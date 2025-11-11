from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('headunits/', views.HeadUnitListView.as_view(), name='headunit_list'),
    path('headunits/<int:pk>/', views.HeadUnitDetailView.as_view(), name='headunit_detail'),
]
