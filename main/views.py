from typing import Dict, Union
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from main.models import Lesson, MediaContent
from .forms import LessonForm


def home(request):
    return render(request, 'home.html')


def lessons_list(request, subject):
    lessons = Lesson.objects.filter(subject=subject)
    lesson_name = Lesson.objects.all()
    context = {
        'title': subject,
        'lessons': lessons,
        'lesson_name': lesson_name,
        'url_name': "lesson_page",
    }
    return render(request, 'lessons_list.html', context)


def lesson_view(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    context = {
        "lesson": lesson,
        "url_name": "lesson_page",
    }
    return render(request, 'main/lesson.html', context)


def lesson_create(request):
    error = ' '
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():

            content_file = []
            content_audio = []
            for a in request.FILES.getlist('content_file'):
                content_file.append(MediaContent.objects.create(file=a, title=a.name))
            for a in request.FILES.getlist('content_audio'):
                content_audio.append(MediaContent.objects.create(file=a, title=a.name))
            lesson = form.save(
                commit=False)  # так как commit=False, не сохроняет в базу данных, а создает объект класса
            lesson.author = request.user
            lesson.subject = request.GET.get('subject')
            lesson.save()
            lesson.content_file.add(*content_file)
            lesson.content_audio.add(*content_audio)
            return redirect('home')
        else:
            error = 'Форма заполнена не верно!'

    form = LessonForm()

    context = {
        'form': form,
        'error': error
    }

    return render(request, 'main/lesson_create.html', context)
