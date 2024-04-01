from django.urls import path
from .views import TaskListCreate,TaskRetrieveUpdateDestroy, add

urlpatterns=[
    path('task/',TaskListCreate.as_view(),name='task-list-create'),
    path('task/<int:pk>/',TaskRetrieveUpdateDestroy.as_view(),name='task-retrieve-update-destroy'),
    path('add', add)
]