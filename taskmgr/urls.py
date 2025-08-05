from django.urls import path
from taskmgr.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", TaskListView.as_view(),name='task-list'),
    path('add/',task_add,name='task-add'),
    path('detail/<pk>',TaskDetailView.as_view(),name='task-detail'),
    path('toggle/<pk>',task_toggle,name='task-toggle'),
    path('delete/<pk>',task_del,name='task-delete'),
    path('edit/<pk>',task_ed,name='task-edit'),
    path('signup/', signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
]