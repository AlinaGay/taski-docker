"""
API viewset for managing Task instances.

This module defines a viewset for CRUD operations on Task model instances
using Django REST Framework. It includes a custom destroy method that
returns the serialized data of the deleted task instead of an empty response.
"""


from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer


class TaskView(viewsets.ModelViewSet):
    """A viewset for viewing and editing Task instances."""

    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def destroy(self, *args, **kwargs):
        """Delete a Task instance and return its serialized data."""
        serializer = self.get_serializer(self.get_object())
        super().destroy(*args, **kwargs)
        return Response(serializer.data, status=status.HTTP_200_OK)
