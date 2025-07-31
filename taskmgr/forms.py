from django import forms
from taskmgr.models import Task
class TaskAdd(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title",'text']
