from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import AndroidHeadUnit

class HeadUnitListView(ListView):
    model = AndroidHeadUnit
    template_name = 'mafony/headunit_list.html'
    context_object_name = 'headunits'
    paginate_by = 9

class HeadUnitDetailView(DetailView):
    model = AndroidHeadUnit
    template_name = 'mafony/headunit_detail.html'
    context_object_name = 'headunit'

def home(request):
    featured_headunits = AndroidHeadUnit.objects.filter(in_stock=True)[:6]
    return render(request, 'mafony/home.html', {'featured_headunits': featured_headunits})