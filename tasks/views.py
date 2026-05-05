from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task

# ✅ LANDING PAGE VIEW (THIS WAS MISSING)
def home(request):
    return render(request, 'index.html')


# ✅ DASHBOARD
@login_required
def dashboard(request):
    query = request.GET.get('search')
    category_filter = request.GET.get('category')

    tasks = Task.objects.filter(user=request.user)

    if query:
        tasks = tasks.filter(title__icontains=query)

    if category_filter:
        tasks = tasks.filter(category=category_filter)

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        category = request.POST.get('category')
        due_date = request.POST.get('due_date')

        Task.objects.create(
            user=request.user,
            title=title,
            description=description,
            category=category,
            due_date=due_date if due_date else None
        )

        return redirect('/dashboard/?added=true')

    return render(request, 'tasks/dashboard.html', {'tasks': tasks})


# ✅ COMPLETE TASK
def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = True
    task.save()
    return redirect('/dashboard/?added=true')


# ✅ DELETE TASK
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('/dashboard/?added=true')