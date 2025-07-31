from django.views.generic import ListView
from taskmgr.models import Task
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from .forms import TaskAdd

class TaskListView(ListView):
    model = Task
    context_object_name = "tasks"
    template_name = 'index.html'


def task_add(request):
    if request.method == "POST":
        form = TaskAdd(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = TaskAdd()

    return render(request, "taskform.html", {"form": form})

def task_detail(request,pi):
    task = get_object_or_404(Task,id=pi)
    context = {'task':task}
    return render(request,'taskdetail.html',context)

def task_toggle(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.done = not task.done
    task.save()
    return redirect('task-list')