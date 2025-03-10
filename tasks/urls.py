from django.urls  import path
from .views import create_task, update_task, delete_task, task_all

urlpatterns = [
    path('', task_all, name='task_list'),
    path('new/', create_task, name='task_create'),
    path('<int:pk>/edit/', update_task, name='task_update'),
    path('<int:pk>/delete', delete_task, name='task_delete')
]
