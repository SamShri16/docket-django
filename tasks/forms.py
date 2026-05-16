from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    due_date = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(
            attrs={
                "type": "datetime-local",
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = Task

        fields = [
            "title",
            "description",
            "category",
            "due_date",
        ]

        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Task title"
            }),

            "description": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Description",
                "rows": 4
            }),

            "category": forms.Select(attrs={
                "class": "form-select"
            }),
        }