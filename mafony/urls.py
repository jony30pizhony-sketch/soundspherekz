from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('headunits/', views.HeadUnitListView.as_view(), name='headunit_list'),
    path('headunits/<int:pk>/', views.HeadUnitDetailView.as_view(), name='headunit_detail'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('cart/', views.cart, name='cart'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('checkout/', views.checkout, name='checkout'),
    path('process-payment/', views.process_payment, name='process_payment'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('add-to-wishlist/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('out-of-stock/', views.out_of_stock, name='out_of_stock'),
    path('register/', views.register, name='register'),
]