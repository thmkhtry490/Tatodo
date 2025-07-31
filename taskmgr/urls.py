from django.urls import path
from taskmgr.views import TaskListView

urlpatterns = [
    path("", TaskListView.as_view()),
]