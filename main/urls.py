from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('lessons/<str:subject1>/', views.lessons_list, name='lessons_list'),
    path('create/', views.lesson_create, name='create'),
]
