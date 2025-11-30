from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Q
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import AndroidHeadUnit, Manufacturer

class HeadUnitListView(ListView):
    model = AndroidHeadUnit
    template_name = 'mafony/simple_catalog.html'
   
    context_object_name = 'headunits'
    paginate_by = 9
    ordering = ['name']

    def get_queryset(self):
        queryset = super().get_queryset()
        
        # Search
        search_query = self.request.GET.get('search', '')
        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) |
                Q(manufacturer__name__icontains=search_query)
            )
        
        # Brand filter
        brand_filter = self.request.GET.get('brand', '')
        if brand_filter:
            queryset = queryset.filter(manufacturer__name=brand_filter)
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brands'] = Manufacturer.objects.all()
        context['current_search'] = self.request.GET.get('search', '')
        context['current_brand'] = self.request.GET.get('brand', '')
        return context

class HeadUnitDetailView(DetailView):
    model = AndroidHeadUnit
    template_name = 'mafony/headunit_detail.html'
    context_object_name = 'headunit'

def home(request):
    featured_headunits = AndroidHeadUnit.objects.filter(in_stock=True)[:6]
    return render(request, 'mafony/home.html', {'featured_headunits': featured_headunits})

def about(request):
    return render(request, 'mafony/about.html')

def contacts(request):
    return render(request, 'mafony/contacts.html')

@login_required
def cart(request):
    # Demo data for cart
    cart_items = []
    demo_products = AndroidHeadUnit.objects.filter(in_stock=True)[:2]
    
    for product in demo_products:
        cart_items.append({
            'product': product,
            'quantity': 1,
            'total_price': product.price
        })
    
    total_price = sum(item['total_price'] for item in cart_items)
    
    return render(request, 'mafony/cart.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })

@login_required
def wishlist(request):
    # Demo data for wishlist
    wishlist_items = AndroidHeadUnit.objects.filter(in_stock=True)[:3]
    return render(request, 'mafony/wishlist.html', {
        'wishlist_items': wishlist_items
    })

def add_to_cart(request, product_id):
    product = get_object_or_404(AndroidHeadUnit, id=product_id)
    
    if not product.in_stock:
        return redirect('out_of_stock')
    
    # Demo function - in real app would add to actual cart
    return JsonResponse({
        'status': 'success', 
        'message': 'Product added to cart',
        'cart_count': 1
    })

def remove_from_cart(request, product_id):
    # Demo function
    return JsonResponse({
        'status': 'success', 
        'message': 'Product removed from cart',
        'cart_count': 0
    })

def add_to_wishlist(request, product_id):
    # Demo function
    return JsonResponse({
        'status': 'success', 
        'message': 'Product added to wishlist',
        'action': 'added'
    })

@login_required
def checkout(request):
    # Demo checkout page
    return render(request, 'mafony/checkout.html', {
        'total_price': 25000,
        'cart_items': []
    })

@login_required
def process_payment(request):
    if request.method == 'POST':
        import random
        payment_success = random.choice([True, False])
        
        if payment_success:
            return render(request, 'mafony/payment_success.html', {
                'order_number': f"SOUND-{random.randint(100000, 999999)}"
            })
        else:
            error_type = random.choice(['insufficient_funds', 'invalid_card', 'network_error'])
            return render(request, 'mafony/payment_error.html', {
                'error_type': error_type
            })
    
    return redirect('checkout')

def out_of_stock(request):
    return render(request, 'mafony/error_out_of_stock.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

# Error handlers
def custom_404(request, exception):
    return render(request, '404.html', status=404)

def custom_500(request):
    return render(request, '500.html', status=500)

def custom_403(request, exception):
    return render(request, '403.html', status=403)