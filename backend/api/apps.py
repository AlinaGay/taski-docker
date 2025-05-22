"""
App configuration for the API application.

This module defines the configuration class for the 'api' Django app.
"""


from django.apps import AppConfig


class ApiConfig(AppConfig):
    """Configuration class for the 'api' Django application."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
