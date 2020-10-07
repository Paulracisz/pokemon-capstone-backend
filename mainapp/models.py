from django.db import models


class Pokemon(models.Model):
    poke_ball = models.IntegerField(default=0)
    great_ball = models.IntegerField(default=0)
    ultra_ball = models.IntegerField(default=0)
    master_ball = models.IntegerField(default=0)
    exp = models.IntegerField(default=0)
    currency = models.IntegerField(default=0)
    level = models.IntegerField(default=0)
    