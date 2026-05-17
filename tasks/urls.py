from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),

    path('tasks/', views.task_list, name='task_list'),

    path('add-task/', views.add_task, name='add_task'),
]