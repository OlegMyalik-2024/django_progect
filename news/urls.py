from .import views
from django.urls import path

# Подключение наших страниц приложения news
urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('add', views.add, name='add'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='detail'),
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name='update_news'),
    path('<int:pk>/delete', views.NewsDeleteView.as_view(), name='delete_news'),
    path('register', views.RegisterFormView.as_view(), name='register'),
    path('login', views.LoginFormView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('password-change', views.PasswordChangeView.as_view(), name='password_change')
]