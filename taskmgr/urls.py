from django.urls import path
from taskmgr.views import TaskListView,task_add,task_detail,task_toggle

urlpatterns = [
    path("", TaskListView.as_view(),name='task-list'),
    path('add',task_add,name='task-add'),
    path('detail/<pi>',task_detail,name='task-detail'),
    path('toggle/<pk>',task_toggle,name='task-toggle'),
]