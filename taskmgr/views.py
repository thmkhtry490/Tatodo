from django.views.generic import ListView
from taskmgr.models import Task

class TaskListView(ListView):
    model = Task
    context_object_name = tasks
    template_name = 'index.html'
