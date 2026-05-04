from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task

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
        return redirect('/dashboard/')

    context = {
        'tasks': tasks
    }

    return render(request, 'tasks/dashboard.html', context)


