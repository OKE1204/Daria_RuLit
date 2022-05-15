from typing import Dict, Union
from django.shortcuts import render, redirect, HttpResponseRedirect
from main.models import Lesson, MediaContent
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
            content_file = []
            content_audio = []
            for a in request.FILES.getlist('content_file'):
                content_file.append(MediaContent.objects.create(file=a, title=a.name))
            for a in request.FILES.getlist('content_audio'):
                content_audio.append(MediaContent.objects.create(file=a, title=a.name))
            lesson = form.save(commit=False) #так как commit=False, не сохроняет в базу данных, а создает объект класса
            lesson.author = request.user
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


# def upload_file(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             content_file(request.FILES['file'])
#             return HttpResponseRedirect('/success/url/')
#     else:
#         form = UploadFileForm()
#     return render(request, 'main/lesson_create.html', {'form': form})




# def lesson_create(request):
#     error = ' '
#     if request.method == 'POST' and request.FILES['content_file'] and request.FILES['content_audio'] :
#         form = LessonForm(request.POST)
#         if form.is_valid():
#             form.content_audio = request.FILES('lessonaudio')
#             form.content_file = request.FILES('lessonfile')
#             filesave = FileSystemStorage()
#             filename = filesave.save(name="content_file", content='lessonfile')
#             audioname = filesave.save(name="content_audio", content='lessonaudio')
#             uploaded_file_url = filesave.url(filename)
#             uploaded_audio_url = filesave.url(audioname)
#             form.author = request.user
#             form.save()
#             return redirect('home', {uploaded_file_url, uploaded_audio_url})
#         else:
#             error = 'Форма заполнена не верно!'
#
#     form = LessonForm()
#
#     context = {
#         'form': form,
#         'error': error
#         }
#
#     return render(request, 'main/lesson_create.html', context)
