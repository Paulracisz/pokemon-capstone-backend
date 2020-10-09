from django.db import models

class Pokemon(models.Model):
    name = models.CharField(max_length = 40)
       # Images
    front_normal_image = models.CharField(max_length = 100)
    front_shiny_image = models.CharField(max_length = 100)
    # Stats
    hp = models.IntegerField(default = 0)
    attack = models.IntegerField(default = 0)
    defense = models.IntegerField(default = 0)
    special_attack = models.IntegerField(default = 0)
    special_defense = models.IntegerField(default = 0)
    speed = models.IntegerField(default = 0)
    # Abilities
    ability_One = models.CharField(max_length = 40)
    ability_Two = models.CharField(max_length = 40)
    ability_Three = models.CharField(max_length = 40)
    # Types
    type_One = models.CharField(max_length = 40)
    type_Two = models.CharField(max_length = 40)
    # Base XP
    base_experience = models.IntegerField(default = 0)
