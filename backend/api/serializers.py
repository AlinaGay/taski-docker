"""
Serializer for the Task model.

Defines how Task instances are converted to and from JSON representations
using Django REST Framework.
"""


from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Serializer for the Task model."""

    class Meta:
        """Metadata for the TaskSerializer."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
