from django.shortcuts import render
from .models import Articles
from .forms import ArticlesForm

# Методы
def news_home(request):
    # Метод вывода определенного количества записей из таблицы БД
    news = Articles.objects.order_by('-title')[:5]
    # Метод вывода всех записей из таблицы БД
    news = Articles.objects.all()
    return render(request, 'news/news_home.html', {'news': news})

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