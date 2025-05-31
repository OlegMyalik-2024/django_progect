from .import views
from django.urls import path
from django.contrib.auth.decorators import login_required

# Подключение наших страниц приложения news
urlpatterns = [
    path('', views.news_home, name='news_home'),
    #Cтраницы только для авторизованных пользователей login_required() применяется только к методам которые не 
    # являются представлениями класса
    path('add', login_required(views.add), name='add'),
    #Динамические страницы на основе класса представления только для авторизованных пользователей
    path('<int:pk>', views.NewsDetailView.as_view(), name='detail'),
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name='update_news'),
    path('<int:pk>/delete', views.NewsDeleteView.as_view(), name='delete_news'),  
] 