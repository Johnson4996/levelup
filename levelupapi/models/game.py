"""Game model module"""
from django.db import models


class Game(models.Model):
    """Game database model"""
    gamer = models.ForeignKey("Game", on_delete=models.CASCADE)
    number_of_players = models.IntegerField()
    game_type = models.ForeignKey("GameType", on_delete=models.CASCADE)
    title = models.CharField(max_length=75)
    skill_level = models.IntegerField()