from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Task


# LANDING PAGE
def landing_page(request):
    return render(request, 'landing.html')


# REGISTER
def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {
                'error': 'Username already exists'
            })

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        user.save()

        return redirect('login')

    return render(request, 'register.html')


# LOGIN
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('dashboard')

        return render(request, 'login.html', {
            'error': 'Invalid username or password'
        })

    return render(request, 'login.html')


# LOGOUT
def logout_view(request):
    logout(request)
    return redirect('landing')


# DASHBOARD
@login_required
def dashboard(request):
    tasks = Task.objects.filter(user=request.user).order_by('-id')[:5]

    total_tasks = Task.objects.filter(user=request.user).count()

    completed_tasks = Task.objects.filter(
        user=request.user,
        completed=True
    ).count()

    pending_tasks = Task.objects.filter(
        user=request.user,
        completed=False
    ).count()

    context = {
        'tasks': tasks,
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'pending_tasks': pending_tasks,
    }

    return render(request, 'dashboard.html', context)


# ADD TASK
@login_required
def add_task(request):
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

        return redirect('my_tasks')

    return render(request, 'add_task.html')


# MY TASKS
@login_required
def my_tasks(request):
    tasks = Task.objects.filter(user=request.user).order_by('-id')

    return render(request, 'my_tasks.html', {
        'tasks': tasks
    })


# COMPLETE TASK
@login_required
def complete_task(request, task_id):
    task = get_object_or_404(
        Task,
        id=task_id,
        user=request.user
    )

    task.completed = True
    task.save()

    return redirect('my_tasks')


# DELETE TASK
@login_required
def delete_task(request, task_id):
    task = get_object_or_404(
        Task,
        id=task_id,
        user=request.user
    )

    task.delete()

    return redirect('my_tasks')


# PROFILE PAGE
@login_required
def profile_page(request):
    return render(request, 'profile.html')