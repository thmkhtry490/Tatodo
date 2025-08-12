from django.views.generic import ListView,DetailView
from taskmgr.models import Task
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from mytodolist.settings import SIGNUP_ENABLE
from .forms import TaskAdd,SignUp,ProfileSettings
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.views.generic.edit import FormView

class TaskListView(LoginRequiredMixin, ListView): # Here use generic list view
    model = Task
    context_object_name = "tasks" # Set name of contexts  for send to templates
    template_name = 'index.html'
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'taskdetail.html'
    context_object_name = 'task'
    pk_url_kwarg = 'pk' # Set name of id for send to templates
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

@login_required(login_url='login')
def task_add(request):
    if request.method == "POST": # check form send with post method
        form = TaskAdd(request.POST) # save TaskAdd form in variable
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return HttpResponseRedirect("/") #Go to homepage past of send form
    else:
        form = TaskAdd()

    return render(request, "taskform.html", {"form": form})
class TaskAddView(LoginRequiredMixin, FormView):
    template_name = "taskform.html"
    form_class = TaskAdd
    success_url = "/"
    def form_valid(self,form):
        task = form.save(commit=False)
        task.user = self.request.user
        task.save()
        return super().form_valid(form) 

@login_required(login_url='login')
def task_toggle(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.done = not task.done #swap in task status
    task.save()
    return redirect(request.META.get('HTTP_REFERER', '/'))

@login_required(login_url='login')
def task_del(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('task-list')

@login_required(login_url='login')
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


def signup(request):
    if not SIGNUP_ENABLE:
        raise PermissionDenied("You can't signup because admin has closed it.")

    if request.user.is_authenticated:
        raise PermissionDenied("You're logged in.")

    if request.method == "POST":
        form = SignUp(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUp()

    return render(request, 'signup.html', {'form': form})


@login_required
def profile_settings(request):
    user = request.user
    if request.method == "POST":
        user_form = ProfileSettings(request.POST, instance=user)
        pwd_form = PasswordChangeForm(user, request.POST)
        if 'save_info' in request.POST and user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your profile was updated.')
            return redirect('user-settings')
        elif 'change_password' in request.POST and pwd_form.is_valid():
            pwd_form.save()
            update_session_auth_hash(request, pwd_form.user)
            messages.success(request, 'Password changed successfully.')
            return redirect('user-settings')
    else:
            user_form = ProfileSettings(instance=user)
            pwd_form = PasswordChangeForm(user)

    return render(request, 'profile-settings.html', {
        'user_form': user_form,
        'pwd_form': pwd_form
    })
            
@login_required
def delete_account(request):
    if request.method == 'POST':
        request.user.delete()
        return redirect('login')
    return render(request, 'delete-account.html')
