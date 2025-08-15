from django.urls import path
from taskmgr.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", TaskListView.as_view(),name='task-list'),
    path('add/',TaskAddView.as_view(),name='task-add'),
    path('detail/<pk>',TaskDetailView.as_view(),name='task-detail'),
    path('toggle/<pk>',TaskToggleView.as_view(),name='task-toggle'),
    path('delete/<pk>',TaskDeleteView.as_view(),name='task-delete'),
    path('edit/<pk>',TaskEditView.as_view(),name='task-edit'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html',redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile-settings/',ProfileSettingsView.as_view(),name='profile-settings'),
    path('profile-settings/delete-account/',DeleteAccount.as_view(),name='delete-account'),

]