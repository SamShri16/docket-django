from django.contrib import admin
from django.urls import path, include
from tasks.views import landing_page

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', landing_page, name='landing'),

    path('', include('tasks.urls')),

    path('accounts/', include('django.contrib.auth.urls')),
]