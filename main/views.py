from django.shortcuts import render, redirect
from main.models import Lesson
from .forms import LessonForm


def home(request):
    return render(request, 'home.html')


def lessons_list(request, subject1):
    lessons = Lesson.objects.filter(subject=subject1)
    context = {'title': subject1, 'lessons': lessons}
    return render(request, 'lessons_list.html', context)


def lesson_create(request):
    error = ' '
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма заполнена не верно!'

    form = LessonForm()

    context = {
        'form': form,
        'error': error
        }

    return render(request, 'main/lesson_create.html', context)
