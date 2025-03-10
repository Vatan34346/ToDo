from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

# Create your views here.


def task_all(req):
    tasks = Task.objects.all()
    return render(req, 'tasks/tasks_list.html', {'tasks': tasks})


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
