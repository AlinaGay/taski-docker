"""
Admin configuration for the Task model.

This module registers the Task model with the Django admin interface,
using the TaskAdmin class to customize its display.

Displayed fields in the list view:
- title
- description
- completed
"""


from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    """Task Admin class."""

    list_display = ('title', 'description', 'completed')


admin.site.register(Task, TaskAdmin)
