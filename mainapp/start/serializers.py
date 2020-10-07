from mainapp import models
from rest_framework import serializers

class PokemonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Pokemon
        fields = ['name', 'front_normal_image', 'front_shiny_image', 'hp', 'attack', 'defense', 'special_attack', 'special_defense', 'speed', 'ability_One', 'ability_Two', 'type_One', 'type_Two']