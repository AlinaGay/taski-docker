"""
Defines the Task model for representing to-do items.

Includes fields for title, description, and completion status.
"""


from django.db import models


class Task(models.Model):
    """Model representing a task or to-do item."""

    title = models.CharField(verbose_name='Заголовок', max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def _str_(self):
        return self.title
