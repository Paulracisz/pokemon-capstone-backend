from mainapp import models
from rest_framework import serializers


class PokemonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Pokemon
        
        fields = ['name', 'front_normal_image', 'ability_One', 'ability_Two',
                  'ability_Three', 'type_One', 'type_Two', 'base_experience']
