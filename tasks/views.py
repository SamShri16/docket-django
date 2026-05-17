from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task


def landing_page(request):
    return render(request, 'landing.html')


@login_required
def dashboard(request):
    tasks = Task.objects.filter(user=request.user)

    total_tasks = tasks.count()
    completed_tasks = tasks.filter(completed=True).count()
    pending_tasks = tasks.filter(completed=False).count()

    recent_tasks = tasks.order_by('-id')[:5]

    context = {
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'pending_tasks': pending_tasks,
        'recent_tasks': recent_tasks,
    }

    return render(request, 'tasks/dashboard.html', context)


@login_required
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        Task.objects.create(
            user=request.user,
            title=title,
            description=description
        )

        return redirect('my_tasks')

    return render(request, 'tasks/add_task.html')


@login_required
def my_tasks(request):
    tasks = Task.objects.filter(user=request.user).order_by('-id')

    return render(request, 'tasks/tasks.html', {
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

@login_required
def task_list(request):
    return render(request, 'tasks/task_list.html')