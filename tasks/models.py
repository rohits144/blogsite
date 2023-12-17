from django.db import models

# Create a model called Task
# with a fields name, description, repeatable, frequency, status, and created_at, updated_at
# name: CharField with max length of 255, not null and unique
# description: TextField, can be blank, 
# repeatable: BooleanField, default to False
# frequency choices: None, daily, weekly, monthly, yearly, custom
# status choices: todo, doing, done
# created_at: DateTimeField, auto_now_add=True
# updated_at: DateTimeField, auto_now=True


class Task(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    repeatable = models.BooleanField(default=False)
    frequency = models.CharField(max_length=255, choices=(('None', 'None'), ('daily', 'daily'), ('weekly', 'weekly'), ('monthly', 'monthly'), ('yearly', 'yearly'), ('custom', 'custom')))
    status = models.CharField(max_length=255, choices=(('todo', 'todo'), ('doing', 'doing'), ('done', 'done')))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
