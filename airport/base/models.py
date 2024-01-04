"""This file includes database models of project."""
from django.db import models


class Airline(models.Model):
    """Airline model class."""

    name = models.CharField(max_length=200)
    callsign = models.CharField(max_length=200)
    founded_year = models.IntegerField()
    base_airport = models.CharField(max_length=20)

    def __str__(self):
        """Name given as str."""
        return self.name


class Aircraft(models.Model):
    """Aircraft model class."""

    manufacturer_serial_number = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    number_of_engines = models.IntegerField()
    operator_airline = models.ForeignKey(Airline,
                                         on_delete=models.CASCADE,
                                         related_name='aircraft_set')

    def __str__(self):
        """Type given as str."""
        return self.type
