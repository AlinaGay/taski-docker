"""
URL routing configuration for the Django project.

This module defines the URL patterns for the Django admin interface and
the API views, using Django REST Framework's router to automatically generate
URLs for the 'Task' viewset.

Includes:
- Admin panel URL at '/admin/'.
- API endpoint for tasks at '/api/tasks/'.
"""


from api import views
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register('tasks', views.TaskView, 'task')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
