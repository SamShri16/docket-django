from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    TASK_TYPE_CHOICES = [
        ('daily', 'Daily'),
        ('normal', 'Normal'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    task_type = models.CharField(max_length=10, choices=TASK_TYPE_CHOICES, default='normal')
    created_at = models.DateTimeField(auto_now_add=True)
    
    reminder_time = models.TimeField(null=True, blank=True)


    def __str__(self):
        return self.title


