"""
Automated tests for the Task API.

This module uses Django's test framework to verify the functionality of
the task list endpoint and task creation through the REST API.
"""


from http import HTTPStatus

from api import models
from django.test import Client, TestCase


class TaskiAPITest(TestCase):
    """Test case for the Task API endpoints."""

    def setUp(self):
        """Set up a test client for use in API requests."""
        self.guest_cleint = Client()

    def test_list_exist(self):
        """Checking the availability of the task list."""
        response = self.guest_cleint.get('/api/tasks/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_task_creation(self):
        """Checking task creation."""
        data = {'title': 'Test', 'description': 'Test'}
        response = self.guest_cleint.post('/api/tasks/', data=data)
        self.assertEqual(response.status_code, HTTPStatus.CREATED)
        self.assertTrue(models.Task.objects.filter(title='Test').exists())
