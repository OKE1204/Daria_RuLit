from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Lesson(models.Model):
    SUBJECTS = (
        ('russian', 'Русский язык'),
        ('literature', 'Литература'),
    )

    name = models.CharField(max_length=50, verbose_name="Наименование урока")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="lessons")
    date_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации урока")
    date_update = models.DateTimeField(auto_now=True, verbose_name="Дата редактирования урока")
    content = models.TextField(verbose_name="Материалы урока")
    content_file = models.ManyToManyField('MediaContent', related_name="content_file", verbose_name="Документы урока")
    content_audio = models.ManyToManyField('MediaContent', related_name="content_audio", verbose_name="Аудио урока")
    subject = models.CharField(max_length=50, choices=SUBJECTS)

    def get_absolut_url(self):
        return f'lessons/{self.id}'


class MediaContent(models.Model):
    title = models.CharField(max_length=50)
    file = models.FileField(upload_to='mediacontent')

# class HomeWork:
#
#
# class LessonStudents:
#
