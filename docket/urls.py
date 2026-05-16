from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from tasks.views import (
    landing_page,
    dashboard,
    add_task,
    complete_task,
    delete_task,
)

from accounts.views import register

urlpatterns = [
    path('admin/', admin.site.urls),

    # Landing Page
    path('', landing_page, name='landing'),

    # Dashboard
    path('dashboard/', dashboard, name='dashboard'),

    # Task Actions
    path('add/', add_task, name='add_task'),
    path('complete/<int:task_id>/', complete_task, name='complete_task'),
    path('delete/<int:task_id>/', delete_task, name='delete_task'),

    # Auth
    path(
        'accounts/login/',
        auth_views.LoginView.as_view(
            template_name='accounts/login.html'
        ),
        name='login'
    ),

    path('accounts/register/', register, name='register'),

    path(
        'accounts/logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),
]