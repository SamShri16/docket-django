from django.contrib import admin
from django.urls import path, include
from tasks.views import home




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('', include('tasks.urls')),
    path('accounts/', include('accounts.urls')),
    path('dashboard/', include('tasks.urls')),
    


]