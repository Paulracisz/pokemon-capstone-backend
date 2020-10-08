from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

    
class PokemonTrainer(AbstractUser):
    displayname = models.CharField(max_length=80)
    personal_website = models.URLField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    pokedexed = models.ManyToManyField('Pokemon', related_name="pokemon_indexed", symmetrical=False, blank=True)
    poke_ball = models.IntegerField(default=5)
    great_ball = models.IntegerField(default=0)
    ultra_ball = models.IntegerField(default=0)
    master_ball = models.IntegerField(default=0)
    exp = models.IntegerField(default=0)
    currency = models.IntegerField(default=0)
    level = models.IntegerField(default=0)


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
    
    def __str__(self):
        return self.name
    

    
