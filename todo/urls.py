from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskList.as_view(), name='task-list'),
    path('task/new/', views.TaskCreate.as_view(), name='task-create'),
    path('task/<int:pk>/update/', views.TaskUpdate.as_view(), name='task-update'),
    path('task/<int:pk>/delete/', views.TaskDelete.as_view(), name='task-delete'),
]