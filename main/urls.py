from .import views
from django.urls import path, re_path
from django.contrib.auth.decorators import login_required

# Подключение наших страниц приложения main
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contacts', views.contacts, name='contacts'),
    path('services', views.services, name='services'),
    path('register', views.RegisterFormView.as_view(), name='register'),
    path('login', views.LoginFormView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    #Cтраницы только для авторизованных пользователей login_required() применяется только к методам которые не 
    # являются представлениями класса
    path('password_change', login_required(views.PasswordChangeView.as_view()), name='password_change'),
]