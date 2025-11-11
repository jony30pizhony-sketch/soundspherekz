from django.urls import path
from . import api_views

urlpatterns = [
    path('headunits/', api_views.HeadUnitListAPIView.as_view(), name='api_headunit_list'),
    path('headunits/<int:pk>/', api_views.HeadUnitDetailAPIView.as_view(), name='api_headunit_detail'),
]