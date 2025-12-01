from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Форма логина (GET/POST) - работает через встроенный LoginView
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # Форма регистрации (GET/POST)
    path('register/', views.register, name='register'),
    # Личный кабинет после входа
    path('profile/', views.profile, name='profile'),
]