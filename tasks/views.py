from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .models import Task
from .forms import TaskForm

# Create your views here.


class TaskListView(ListView):
    model = Task
    template_name = 'tasks/tasks_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        queryset = super().get_queryset()
        status_filter = self.request.GET.get("status")
        if status_filter:
            queryset = queryset.filter(status=status_filter)
        return queryset


def task_list(request):
    status_filter = request.GET.get('status', None)  # Получаем статус из параметра запроса
    if status_filter:
        tasks = Task.objects.filter(status=status_filter)
    else:
        tasks = Task.objects.all()

    return render(request, 'tasks/tasks_list.html', {'tasks': tasks})


def create_task(req):
    if req.method == 'POST':
        form = TaskForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()

    return render(req, 'tasks/task_form.html', {'form': form})


def update_task(req, pk):
    task = get_object_or_404(Task, pk=pk)
    if req.method == 'POST':
        form = TaskForm(req.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)

    return render(req, 'tasks/task_form.html', {'form': form})


def delete_task(req, pk):
    task = get_object_or_404(Task, pk=pk)
    if req.method == 'POST':
        task.delete()
        return redirect('task_list')

    return render(req, 'tasks/task_confirm_delete.html', {'task': task})

