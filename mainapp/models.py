from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class PokemonTrainer(AbstractUser):
    displayname = models.CharField(max_length=80, blank=True, null=True)
    email_address = models.EmailField(blank=True, null=True)
    personal_website = models.URLField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    poke_ball = models.IntegerField(default=5)
    great_ball = models.IntegerField(default=0)
    ultra_ball = models.IntegerField(default=0)
    master_ball = models.IntegerField(default=0)
    exp = models.IntegerField(default=0)
    currency = models.IntegerField(default=0)
    level = models.IntegerField(default=0)


class Pokemon(models.Model):

    name = models.CharField(max_length=40)
    front_normal_image = models.CharField(max_length=100)

    height = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)

    ability_One = models.CharField(max_length=40)
    ability_Two = models.CharField(max_length=40)
    ability_Three = models.CharField(max_length=40)

    type_One = models.CharField(max_length=40)
    type_Two = models.CharField(max_length=40)
    base_experience = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
    
class CaughtPokemon(models.Model):
    owner = models.ForeignKey(PokemonTrainer, on_delete=models.CASCADE, related_name="poke_trainer")
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name="poke")
    date_caught = models.DateTimeField(default=timezone.now)
    
    # def __str__(self):
    #     return self.owner
