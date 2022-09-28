from django import forms
from todolist.models import Task
class TaskCreationForm(forms.ModelForm):
    class Meta:
        model = Task
        fields=['title', 'description']