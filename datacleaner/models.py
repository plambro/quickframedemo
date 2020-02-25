# django imports
from django.db import models


class CleanData(models.Model):
    """Data model for cleaned dataset entries."""

    object_number = models.CharField(max_length=64, unique=False)
    start_date = models.CharField(max_length=64, unique=False)
    end_date = models.CharField(max_length=64, unique=False)

    def __str__(self):
        """Return primary key for string."""
        return f'{self.id}'
