"""Built-in apps.py class."""
from django.apps import AppConfig


class BaseConfig(AppConfig):
    """Built-in appconfig class."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base'
