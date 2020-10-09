from django.db import models


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
