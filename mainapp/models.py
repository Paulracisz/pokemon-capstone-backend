from django.db import models


class Pokemon(models.Model):
    name = models.CharField(max_length=40)
    # Images
    front_normal_image = models.CharField(max_length=100)
    # Stats
    height = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    # Abilities
    ability_One = models.CharField(max_length=40)
    ability_Two = models.CharField(max_length=40)
    ability_Three = models.CharField(max_length=40)
    # Types
    type_One = models.CharField(max_length=40)
    type_Two = models.CharField(max_length=40)
    # Base XP
    base_experience = models.IntegerField(default=0)
