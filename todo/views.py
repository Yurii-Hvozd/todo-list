from django.urls import reverse_lazy
from django.views import generic, View
from django.shortcuts import get_object_or_404, redirect
from todo.forms import TaskForm
from todo.models import Task, Tag



class TaskListView(generic.ListView):
    model = Task

    def get_queryset(self):
        return Task.objects.prefetch_related("tags")


class TaskCreateView(generic.CreateView):
    model = Task

    success_url = reverse_lazy("todo_list:task_list")
    form_class = TaskForm


class TaskUpdateView(generic.UpdateView):
    model = Task

    success_url = reverse_lazy("todo_list:task_list")
    form_class = TaskForm


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo_list:task_list")


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_list:tag_list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_list:tag_list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo_list:tag_list")


class ToggleTaskStatusView(View):
    def post(self, request, pk, *args, **kwargs):
        task = get_object_or_404(Task, id=pk)

        if task.is_done:
            task.is_done = False
        else:
            task.is_done = True

        task.save()

        return redirect('todo_list:task_list')
