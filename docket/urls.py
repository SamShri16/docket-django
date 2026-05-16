from django.contrib import admin
from django.urls import path
from tasks.views import (
    landing_page,
    dashboard,
    complete_task,
    delete_task,
)

from accounts.views import register_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', landing_page, name='landing'),

    path('dashboard/', dashboard, name='dashboard'),

    path('complete/<int:task_id>/', complete_task, name='complete'),

    path('delete/<int:task_id>/', delete_task, name='delete'),

    path(
        'accounts/login/',
        auth_views.LoginView.as_view(
            template_name='registration/login.html'
        ),
        name='login'
    ),

    path('accounts/register/', register_view, name='register'),

    path(
        'accounts/logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),
]