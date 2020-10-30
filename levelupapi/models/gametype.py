"""Game type model module"""
from django.db import models

class GameType(models.Model):
    """Game type database module"""
    label = models.CharField(max_length=25)