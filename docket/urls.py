from django.contrib import admin
from django.urls import path
from tasks.views import (
    landing_page,
    dashboard,
    add_task,
    my_tasks,
    complete_task,
    delete_task,
    profile_page,
    register_view,
    login_view,
    logout_view,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Landing page
    path('', landing_page, name='landing'),

    # Auth
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),

    # Dashboard
    path('dashboard/', dashboard, name='dashboard'),
    path('dashboard/add/', add_task, name='add_task'),
    path('dashboard/tasks/', my_tasks, name='my_tasks'),
    path('dashboard/profile/', profile_page, name='profile'),

    # Task actions
    path('complete/<int:task_id>/', complete_task, name='complete_task'),
    path('delete/<int:task_id>/', delete_task, name='delete_task'),
]