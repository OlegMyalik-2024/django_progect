from django.db import models

# Создание таблицы БД
class Articles(models.Model):
    title = models.CharField('Название', max_length=50)
    full_text = models.TextField('Ссылка')
    
    # Вывод новостей в строковом представлении
    def __str__(self):
        return self.title
    #Переадресация пользователя после обновления новости
    def get_absolute_url(self):
        return f'/news/{self.id}'
    
    
    # Задать название таблицы
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        
    # username: admin
    # password: Hgggght97107