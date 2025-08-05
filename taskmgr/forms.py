from django import forms
from taskmgr.models import Task
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class TaskAdd(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title",'text']

class SignUp(UserCreationForm):
    class Meta:
        model = User
        fields = ("first_name","last_name","username")