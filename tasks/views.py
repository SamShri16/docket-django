from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def landing_page(request):
    return render(request, 'landing.html')


@login_required
def dashboard(request):
    return render(request, 'tasks/dashboard.html')


@login_required
def task_list(request):
    return render(request, 'tasks/task_list.html')


@login_required
def add_task(request):
    return render(request, 'tasks/add_task.html')