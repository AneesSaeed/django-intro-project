from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView

from task.forms import TaskForm

from .models import Task


class TaskView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Task
    template_name = 'task/task.html'
    context_object_name = "tasks"

    permission_required = 'task.task_management'

    def get_context_data(self, **kwargs):
        context = super(TaskView, self).get_context_data(**kwargs)
        context['form'] = TaskForm
        return context


def create(request, pk=None):
    data = request.POST.copy()
    if pk and not data.get("assignee"):
        data["assignee"] = pk
    form = TaskForm(data)
    if form.is_valid():
        form.save()

    return redirect('task:index')


def delete(request, pk):
    if request.method == "POST":
        task = get_object_or_404(Task, pk=pk)
        task.delete()

    return redirect('task:index')