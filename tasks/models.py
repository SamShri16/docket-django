from django.db import models
from django.contrib.auth.models import User

CATEGORY_CHOICES = [
    ('Work', 'Work'),
    ('Home', 'Home'),
    ('Daily', 'Daily'),
    ('Study', 'Study'),
]

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Work')

    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank=True)

    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    


    