from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task


def landing_page(request):
    return render(request, 'tasks/landing.html')


@login_required
def dashboard(request):
    tasks = Task.objects.filter(user=request.user)

    completed_tasks = tasks.filter(completed=True)
    pending_tasks = tasks.filter(completed=False)

    context = {
        'tasks': tasks,
        'completed_count': completed_tasks.count(),
        'pending_count': pending_tasks.count(),
        'recent_tasks': tasks.order_by('-id')[:5],
    }

    return render(request, 'tasks/dashboard.html', context)


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

    return render(request, 'tasks/add_task.html')


@login_required
def my_tasks(request):
    tasks = Task.objects.filter(user=request.user)

    return render(request, 'tasks/my_tasks.html', {
        'tasks': tasks
    })


@login_required
def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)

    task.completed = True
    task.save()

    return redirect('my_tasks')


@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)

    task.delete()

    return redirect('my_tasks')