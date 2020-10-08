from django.shortcuts import render
from rest_framework import viewsets
from mainapp import serializers, models

# Create your views here.

class PokemonTrainerViewSet(viewsets.ModelViewSet):
    queryset = models.PokemonTrainer.objects.all()
    serializer_class = serializers.PokemonTrainerSerializer
    
class PokemonViewSet(viewsets.ModelViewSet):
    queryset = models.Pokemon.objects.all()
    serializer_class = serializers.PokemonSerializer