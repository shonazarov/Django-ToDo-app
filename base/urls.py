from unicodedata import name
from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import (
    TaskDeleteView,TaskListViews,
    TaskDetailView, TaskCreateView, TaskUpdateView,
    CustomLoginView, RegisterPage
    )



urlpatterns = [
    path('register/', RegisterPage.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    path('', TaskListViews.as_view(), name='tasks'),
    path('task/<str:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('task-create/', TaskCreateView.as_view(), name='create'),
    path('task-update/<int:pk>', TaskUpdateView.as_view(), name='task-update'),
    path('task-delete/<int:pk>', TaskDeleteView.as_view(), name='task-delete'),

]