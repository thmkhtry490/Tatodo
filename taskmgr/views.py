from django.views.generic import ListView,DetailView
from taskmgr.models import Task
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from .forms import TaskAdd

class TaskListView(ListView):
    model = Task
    context_object_name = "tasks"
    template_name = 'index.html'

class TaskDetailView(DetailView):
    model = Task
    template_name = 'taskdetail.html'
    context_object_name = 'task'
    pk_url_kwarg = 'pi'

def task_add(request):
    if request.method == "POST":
        form = TaskAdd(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = TaskAdd()

    return render(request, "taskform.html", {"form": form})

def task_toggle(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.done = not task.done
    task.save()
    return redirect('task-list')
def task_del(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('task-list')