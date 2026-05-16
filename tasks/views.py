from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task


def home(request):
    return render(request, 'index.html')


@login_required
def dashboard(request):
    tasks = Task.objects.filter(user=request.user, completed=False)[:5]
    return render(request, 'tasks/dashboard_home.html', {'tasks': tasks})


@login_required
def add_task(request):
    if request.method == 'POST':
        Task.objects.create(
            user=request.user,
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            category=request.POST.get('category'),
            due_date=request.POST.get('due_date') or None
        )
        return redirect('/dashboard/tasks/')

    return render(request, 'tasks/add_task.html')


@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = True
    task.save()
    return redirect('/dashboard/tasks/')


def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('/dashboard/tasks/')