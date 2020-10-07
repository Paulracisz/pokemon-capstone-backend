from django.db import models

class Pokemon(models.Model):
    # Pokemon Name
    name = models.CharField(max_length = 40)
    # Images
    front_normal_image = models.CharField(max_length = 100)
    front_shiny_image = models.CharField(max_length = 100)
    # Stats
    hp = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    special_attack = models.IntegerField()
    special_defense = models.IntegerField()
    speed = models.IntegerField()
    # Abilities
    ability_One = models.CharField(max_length = 40)
    ability_Two = models.CharField(max_length = 40)
    # Types
    type_One = models.CharField(max_length = 40)
    type_Two = models.CharField(max_length = 40)
    # Base XP
    base_experience = models.IntegerField()
    #Default Pokemon?
    is_default = models.BooleanField(default = 0)
    # Leave a comment about your pokemon
    your_thoughts = models.TextField(blank = True)
    # Details about this pokemon can be found at:
    details_at = models.URLField()

# Create your models here.
