from .models import Lesson
from django.forms import ModelForm, Textarea


class LessonForm(ModelForm):
    class Meta:
        model = Lesson
        fields = ["name", "content"]
        widgets = {
            "name": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название урока'
            }),
            "content": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание урока'
            }),
        }
