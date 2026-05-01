from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task

@login_required
def home(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST.get('description', '')
        task_type = request.POST.get('task_type', 'normal')

        Task.objects.create(
            user=request.user,
            title=title,
            description=description,
            task_type=task_type
        )

        return redirect('home')

    tasks = Task.objects.filter(user=request.user)

    daily_tasks = tasks.filter(task_type='daily')
    normal_tasks = tasks.filter(task_type='normal')

    total_tasks = tasks.count()
    completed_tasks = tasks.filter(completed=True).count()
    pending_tasks = tasks.filter(completed=False).count()

    context = {
        'daily_tasks': daily_tasks,
        'normal_tasks': normal_tasks,
        'total': total_tasks,
        'completed': completed_tasks,
        'pending': pending_tasks
    }

    return render(request, 'home.html', context)


@login_required
def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.completed = True
    task.save()
    return redirect('home')


@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.delete()
    return redirect('home')