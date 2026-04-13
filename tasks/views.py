from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task

@login_required
def home(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST.get('description', '')

        Task.objects.create(
            user=request.user,
            title=title,
            description=description
        )

        return redirect('home')

    tasks = Task.objects.filter(user=request.user)
    return render(request, 'home.html', {'tasks': tasks})


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