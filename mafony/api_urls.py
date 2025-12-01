from django.urls import path
from . import api_views

# API эндпоинты для магнитол (книг)
# Требование: /api/mafony/ возвращает список книг в JSON
# Требование: /api/mafony/<id>/ возвращает детали книги
urlpatterns = [
    # Эндпоинт /api/mafony/ возвращает список магнитол в JSON
    path('mafony/', api_views.HeadUnitListAPIView.as_view(), name='api_headunit_list'),
    # Эндпоинт /api/mafony/<id>/ возвращает детали магнитолы
    path('mafony/<int:pk>/', api_views.HeadUnitDetailAPIView.as_view(), name='api_headunit_detail'),
]