"""EventGamer model module"""
from django.db import models
from django.db.models.deletion import CASCADE

class EventGamer(models.Model):
    """EventGamer database model"""
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE, related_name="registrations")
    event = models.ForeignKey("Event", on_delete=models.CASCADE, related_name="registrations")