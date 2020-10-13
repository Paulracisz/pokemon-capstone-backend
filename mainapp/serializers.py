from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from mainapp import models


class PokemonTrainerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.PokemonTrainer
        fields = [
            'username',
            'displayname',
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
        
# class PokemonTrainerSerializerWithToken(serializers.ModelSerializer):
    
#     token = serializers.SerializerMethodField()
#     password = serializers.CharField(write_only=True)
    
#     def get_token(self, obj):
#         jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
#         jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        
#         payload = jwt_payload_handler(obj)
#         token = jwt_encode_handler(payload)
        
#     def create(self, validated_data):
#         password = validated_data.pop('password', None)
#         instance = self.Meta.model(**validated_data)
#         if password is not None:
#             instance.set_password(password)
#         instance.save()
#         return instance
    
#     class Meta:
#         model = models.PokemonTrainer
#         fields = ('token', 'username', 'password')


class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pokemon
        fields = ['name', 'front_normal_image', 'ability_One', 'ability_Two',
                  'ability_Three', 'type_One', 'type_Two', 'base_experience']
