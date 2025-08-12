from django.views.generic import ListView,DetailView
from taskmgr.models import Task
from django.shortcuts import render, get_object_or_404, redirect
from mytodolist.settings import SIGNUP_ENABLE
from .forms import TaskAdd,SignUp,ProfileSettings
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from django.views.generic.edit import FormView,DeleteView,UpdateView
from django.views import View
from django.contrib import messages
from django.urls import reverse_lazy


class TaskListView(LoginRequiredMixin, ListView): # Here use generic list view
    """
    It's home page view past login shows list of User tasks.
    """
    model = Task
    context_object_name = "tasks" # Set name of contexts  for send to templates
    template_name = 'index.html'
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

class TaskDetailView(LoginRequiredMixin, DetailView):
    """
    It's task detail page shows information of a task.
    """
    model = Task
    template_name = 'taskdetail.html'
    context_object_name = 'task'
    pk_url_kwarg = 'pk' # Set name of id for send to templates
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

class TaskAddView(LoginRequiredMixin, FormView):
    """
    It's add task page view
    """
    template_name = "taskform.html"
    form_class = TaskAdd
    success_url = "/"
    def form_valid(self,form):
        task = form.save(commit=False)
        task.user = self.request.user
        task.save()
        return super().form_valid(form) 

class ProfileSettingsView(LoginRequiredMixin, View):
    """
    It's Proflies setting View  has 2 forms:
    1. Edit Information of account
    2. Password Change form
    and has delete account button
    """
    template_name = 'profile-settings.html'

    def get(self, request, *args, **kwargs):
        user_form = ProfileSettings(instance=request.user)
        pwd_form = PasswordChangeForm(request.user)
        return render(request, self.template_name, {
            'user_form': user_form,
            'pwd_form': pwd_form
        })

    def post(self, request, *args, **kwargs):
        user_form = ProfileSettings(request.POST, instance=request.user)
        pwd_form = PasswordChangeForm(request.user, request.POST)

        if 'save_info' in request.POST and user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your profile was updated.')
            return redirect('profile-settings')

        elif 'change_password' in request.POST and pwd_form.is_valid():
            pwd_form.save()
            update_session_auth_hash(request, pwd_form.user)
            messages.success(request, 'Password changed successfully.')
            return redirect('profile-settings')

        return render(request, self.template_name, {
            'user_form': user_form,
            'pwd_form': pwd_form
        })
class SignUpView(FormView):
    template_name = "signup.html"
    form_class = SignUp
    success_url = "/"
    def dispatch(self, request, *args, **kwargs):
        if not SIGNUP_ENABLE:
            raise PermissionDenied("You can't signup because admin has closed it.")
        if request.user.is_authenticated:
            raise PermissionDenied("You're logged in.")
        return super().dispatch(request, *args, **kwargs)
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class DeleteAccount(LoginRequiredMixin,DeleteView):
    model = User
    success_url = "/"
    template_name = "delete-account.html"  
    
    def get_object(self, queryset=None):
        return self.request.user

class TaskToggleView(LoginRequiredMixin, View):
    login_url = 'login'

    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.done = not task.done
        task.save()
        return redirect(request.META.get('HTTP_REFERER', '/'))


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = "taskdel.html"
    success_url = "/"
    login_url = 'login'


class TaskEditView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskAdd
    template_name = "taskedit.html"
    login_url = 'login'

    def get_success_url(self):
        return reverse_lazy("task-detail", kwargs={"pk": self.object.pk})

