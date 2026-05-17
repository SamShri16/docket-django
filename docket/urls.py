from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from tasks.views import landing_page

urlpatterns = [
    path('admin/', admin.site.urls),

    # Landing Page
    path('', landing_page, name='landing'),

    # Accounts
    path('accounts/', include('accounts.urls')),

    # Tasks
    path('', include('tasks.urls')),
]