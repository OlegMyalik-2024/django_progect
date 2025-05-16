from .import views
from django.urls import path, re_path

# Подключение наших страниц приложения main
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contacts', views.contacts, name='contacts'),
    path('services', views.services, name='services'),
    path('register', views.RegisterFormView.as_view(), name='register'),
    path('login', views.LoginFormView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('password-change', views.PasswordChangeView.as_view(), name='password_change')
]