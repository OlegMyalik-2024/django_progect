from django.shortcuts import render
from .models import Articles
from .forms import ArticlesForm
# Базовый класс для обработки страниц с формами.
from django.views.generic.edit import FormView
# Спасибо django за готовую форму регистрации.
from django.contrib.auth.forms import UserCreationForm
# Спасибо django за готовую форму аутентификации.
from django.contrib.auth.forms import AuthenticationForm
# Функция для установки сессионного ключа. По нему django будет определять, выполнил ли вход пользователь.
from django.contrib.auth import login
# Для Log out с перенаправлением на главную
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import logout
# Для смены пароля - форма
from django.contrib.auth.forms import PasswordChangeForm

# Базовый URL приложения, главной страницы - часто нужен при указании путей переадресации
app_url = "/"

# Представление для регистрации
class RegisterFormView(FormView):
    # встроенная в django форма регистрации
    form_class = UserCreationForm
    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = app_url + "index"
    # Шаблон, который будет использоваться при отображении представления.
    template_name = "main/reg/register.html"
    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()
        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)

# Наше представление для входа
class LoginFormView(FormView):
    # Будем строить на основе встроенной в django формы входа
    form_class = AuthenticationForm
    # Аналогично регистрации, только используем шаблон аутентификации.
    template_name = "main/reg/login.html"
    # В случае успеха перенаправим на главную.
    success_url = app_url
    def form_valid(self, form):
        # Получаем объект пользователя на основе введённых в форму данных.
        self.user = form.get_user()
        # Выполняем аутентификацию пользователя.
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


# Для выхода - миниатюрное представление без шаблона - после выхода перенаправим на главную
class LogoutView(View):
    def get(self, request):
        # Выполняем выход для пользователя, запросившего данное представление.
        logout(request)
        # После чего перенаправляем пользователя на главную страницу.
        return HttpResponseRedirect(app_url)


# Наше представление для смены пароля
class PasswordChangeView(FormView):
    # Будем строить на основе встроенной в django формы смены пароля
    form_class = PasswordChangeForm
    template_name = 'main/reg/password_change_form.html'
    # После смены пароля нужно снова входить
    success_url = app_url 
    def get_form_kwargs(self):
        kwargs = super(PasswordChangeView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        if self.request.method == 'POST':
            kwargs['data'] = self.request.POST
        return kwargs
    def form_valid(self, form):
        form.save()
        # После смены пароля нужно обновить сессию пользователя, чтобы он не был разлогинен
        login(self.request, self.request.user)
        return super(PasswordChangeView, self).form_valid(form)



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