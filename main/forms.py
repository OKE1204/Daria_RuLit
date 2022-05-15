from .models import Lesson
from django.forms import ModelForm, TextInput, Textarea, Select, FileInput
from django import forms


class LessonForm(ModelForm):
    class Meta:
        model = Lesson
        fields = ["name", "subject", "content"]
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
        }


# def handle_uploaded_file(f):
#     with open('some/file/name.txt', 'wb+') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)
