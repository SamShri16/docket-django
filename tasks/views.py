from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task

from django.shortcuts import render

def home(request):
    return render(request, 'index.html')


@login_required
def home(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST.get('description', '')
        task_type = request.POST.get('task_type', 'normal')
        reminder_time = request.POST.get('reminder_time') or None

        Task.objects.create(
            user=request.user,
            title=title,
            description=description,
            task_type=task_type,
            reminder_time=reminder_time
        )

        return redirect('home')

    tasks = Task.objects.filter(user=request.user)

    context = {
        'daily_tasks': tasks.filter(task_type='daily'),
        'normal_tasks': tasks.filter(task_type='normal'),
        'total': tasks.count(),
        'completed': tasks.filter(completed=True).count(),
        'pending': tasks.filter(completed=False).count()
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