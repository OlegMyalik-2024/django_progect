from django.shortcuts import render
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


# Метод возврата страницы index.html
def index(request):
    data={
        'title': 'Главная страница',
        'header': 'Добро пожаловать к нам!',
        'header1': 'О нас',
        'header2': 'Наши преимущества',
        'title1':{
            't1': 'Высокое качество',
            't2': 'Простота в освоении',
            't3': 'Бесплатное обучение'
        },
        'text':{
            't1': 'Наша организация занимается продвижением онлайн-курсов по изучению языка гипертекстовой '
                  'разметки HTML, и таких популярных языков как CSS и JavaScript.',
            't2': 'Наши курсы постоянно редактируются и перерабатываются в соответствии с современными реалиями.',
            't3': 'Наши курсы строго структурированы в зависимости от сложности преподносимого материала.',
            't4': 'Наши курсы абсолютно бесплатны и доступны для всех желающих. Для получения доступа '
                  'необходимо пройти процедуру регистрации или авторизации.'
        }
    }
    return render(request, 'main/index.html', data)

# Метод возврата страницы about.html
def about(request):
    data={
        'title': 'О нас',
        'header': 'Информация о нас',
        'text': 'Наша организация была основана в 2020 году. Мы занимаемся в основном разработкой программных '
        'продуктов и также периодически размещаем и корректируем обучающие курсы на нашем сайте. '
        'Наши курсы представляют собой базовый пакет знаний, которые необходимы начинающему веб-разработчику '
        'для того чтобы попробовать создать свою первую веб-страницу.'
    }
    return render(request, 'main/about.html', data)

# Метод возврата страницы contacts.html
def contacts(request):
    data={
        'title': 'Контакты',
        'header': 'Контакты',
        'header1': 'Наше местоположение',
        'text':{
            't1': 'Наш адрес: г. Минск, ул. Филимонова, 24',
            't2': 'Наш телефон: +375173572345',
            't3': 'Наш email: www.genesis.com'
        }
    }
    return render(request, 'main/contacts.html', data)

# Метод возврата страницы services.html
def services(request):
    data={
        'title': 'Услуги',
        'header': 'Услуги',
        'headers':{
            'h1': 'Курс HTML',
            'h2': 'Курс CSS',
            'h3': 'Курс JavaScript'
        },
        'text': 'Наша компания предоставляет Вам обучающие курсы со структурированным базовым материалом для изучения таких '
            'языков программирования как HTML, CSS и JavaScript. Для того чтобы получить доступ к курсам необходимо '
            'зарегистрироваться или пройти авторизацию.'
    }
    return render(request, 'main/services.html', data)