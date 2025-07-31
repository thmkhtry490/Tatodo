from django.urls import path
from taskmgr.views import TaskListView,TaskDetailView,task_add,task_toggle, task_del

urlpatterns = [
    path("", TaskListView.as_view(),name='task-list'),
    path('add',task_add,name='task-add'),
    path('detail/<pi>',TaskDetailView.as_view(),name='task-detail'),
    path('toggle/<pk>',task_toggle,name='task-toggle'),
    path('delete/<pk>',task_del,name='task-delete'),
]