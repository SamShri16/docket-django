from django.shortcuts import render, redirect
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