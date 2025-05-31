from django.shortcuts import render
from .models import Articles
from .forms import ArticlesForm
#Создание динамически изменяемых страниц при помощи встроенных классов
from django.views.generic import DetailView, UpdateView, DeleteView
# Декорирование метода для защищенного входа
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Базовый URL приложения, главной страницы - часто нужен при указании путей переадресации
app_url = "/" 

#Создание динамических страниц на основе представления таблицы в БД
#Доступ только для авторизованных пользователей для представлений класса @method_decorator(login_required, name='dispatch')
@method_decorator(login_required, name='dispatch')
class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'

#Представление на основе таблицы БД для обновления записей
@method_decorator(login_required, name='dispatch')
class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/update.html'
    form_class = ArticlesForm
    
#Представление на основе таблицы БД для удаления записей
@method_decorator(login_required, name='dispatch')
class NewsDeleteView(DeleteView):
    model = Articles
    template_name = 'news/delete.html'
    success_url = '/news/'
    

# Методы
def news_home(request):
    # Метод вывода определенного количества записей из таблицы БД
    #news = Articles.objects.order_by('-title')[:5]
    # Метод вывода всех записей из таблицы БД
    news = Articles.objects.all()
    return render(request, 'news/news_home.html', {'news': news})

# метод для защищенного входа только авторизованных пользователей
def add(request):
    error=''
    if request.method=="POST":
        form=ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            error='Новость успешно добавлена в базу данных!'
        else:
            error='Форма неверно заполнена!!!'
    
    form=ArticlesForm()
    data={
        'form': form,
        'error': error
    }
    return render(request, 'news/add.html', data)