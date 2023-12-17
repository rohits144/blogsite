from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .models import Task
from django.views.generic import DetailView

class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_detail.html'  # Specify the template for rendering the task detail
    context_object_name = 'task'  # Specify the variable name to use in the template for the task object

class TaskCreateView(CreateView):
    model = Task
    fields = ['title', 'description', 'due_date']

class TaskUpdateView(UpdateView):
    model = Task
    fields = ['title', 'description', 'due_date']

class TaskDeleteView(DeleteView):
    model = Task
    success_url = '/tasks/'  # Redirect to the task list after deletion

class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'  # Specify the template for rendering the task list
    context_object_name = 'tasks'  # Specify the variable name to use in the template for the task list queryset

