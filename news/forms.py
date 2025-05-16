from .models import Articles
from django.forms import ModelForm, TextInput, Textarea

# Создаем обьект формы на базе таблицы Articles из БД
class ArticlesForm(ModelForm):
    class Meta:
        model=Articles
        fields=['title','full_text']
        
        # Создаем представления полей ввода формы
        widgets={
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Заголовок новости'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Ссылка на статью'
            }),
        }