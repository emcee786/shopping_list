from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={"class":"myinput", "placeholder":"Add Task"}))
    class Meta:
        model = Task
        fields = ["title"]