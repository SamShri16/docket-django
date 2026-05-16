from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Task


def landing_page(request):
    return render(request, 'landing.html')


@login_required
def dashboard(request):
    tasks = Task.objects.filter(user=request.user).order_by('-id')

    completed_count = tasks.filter(completed=True).count()
    pending_count = tasks.filter(completed=False).count()

    context = {
        'tasks': tasks,
        'completed_count': completed_count,
        'pending_count': pending_count,
    }

    return render(request, 'dashboard.html', context)


@login_required
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')

        if title:
            Task.objects.create(
                user=request.user,
                title=title
            )

    return redirect('dashboard')


@login_required
def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)

    task.completed = True
    task.save()

    return redirect('dashboard')


@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)

    task.delete()

    return redirect('dashboard')