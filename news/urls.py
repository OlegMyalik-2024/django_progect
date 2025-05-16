from .import views
from django.urls import path

# Подключение наших страниц приложения news
urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('add', views.add, name='add')
]