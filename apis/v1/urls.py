from django.urls import path
from .views import TaskAPIView
urlpatterns = [
    path('tasks/',TaskAPIView.as_view()),
    path('task/<int:pk>',TaskRetrieveUpdateDestroyAPIView.as_view(), name='task-detail'),
]