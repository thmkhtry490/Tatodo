from django.views.generic import ListView,DetailView
from taskmgr.models import Task
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from .forms import TaskAdd

class TaskListView(ListView): # Here use generic list view
    model = Task
    context_object_name = "tasks" # Set name of contexts  for send to templates
    template_name = 'index.html'

class TaskDetailView(DetailView):
    model = Task
    template_name = 'taskdetail.html'
    context_object_name = 'task'
    pk_url_kwarg = 'pk' # Set name of id for send to templates

def task_add(request):
    if request.method == "POST": # check form send with post method
        form = TaskAdd(request.POST) # save TaskAdd form in variable
        if form.is_valid():
            form.save() 
            return HttpResponseRedirect("/") #Go to homepage past of send form
    else:
        form = TaskAdd()

    return render(request, "taskform.html", {"form": form})

def task_toggle(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.done = not task.done #swap in task status
    task.save()
    return redirect(request.META.get('HTTP_REFERER', '/'))

def task_del(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('task-list')

def task_ed(request,pk):
    task = get_object_or_404(Task,pk=pk)
    if request.method == "POST":
        #instance shows before your changes task in edit form
        form = TaskAdd(request.POST,instance=task) 
        if form.is_valid():
            form.save()
            return redirect("task-detail", pk=pk) # go to task detail page past of edit and save
    else:
        form = TaskAdd(instance=task)

    return render(request, "taskedit.html", {"form": form,"task":task})