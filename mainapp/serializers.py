from rest_framework import serializers

from mainapp import models


class PokemonTrainerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.PokemonTrainer
        fields = [
            'username',
            'password',
            'displayname',
            'email',
            'bio',
            'pokedexed',
            'poke_ball',
            'great_ball',
            'ultra_ball',
            'master_ball',
            'exp',
            'currency',
            'level'
        ]
        
class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pokemon
        fields = [
            'name',
            'front_normal_image',
            'front_shiny_image',
            'hp',
            'attack',
            'defense',
            'special_attack',
            'special_defense',
            'speed',
            'ability_One',
            'ability_Two',
            'base_experience',
            'is_default'
        ]