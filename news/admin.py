from django.contrib import admin
from .models import Articles

# Регистрация таблицы БД в панели администратора
admin.site.register(Articles)
