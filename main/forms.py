from .models import Lesson
from django.forms import ModelForm, TextInput, Textarea, Select, FileInput


class LessonForm(ModelForm):
    class Meta:
        model = Lesson
        fields = ["name", "subject", "content", "content_file", "content_audio"]
        widgets = {
            "name": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название урока'
            }),
            "subject": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Выберете предмет'
            }),
            "content": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание урока'
            }),
            "content_file": FileInput(attrs={
                'class': 'file-input',
                'placeholder': 'Добавте материалы урока'
            }),
            "content_audio": FileInput(attrs={
                'class': 'file-input',
                'placeholder': 'Добавте аудиозапись урока'
            }),
        }
