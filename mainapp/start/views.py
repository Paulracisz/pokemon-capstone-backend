from django.shortcuts import render

# Create your views here.
from mainapp import models
from rest_framework import viewsets
from mainapp.start import serializers

class PokemonViewSet(viewsets.ModelViewSet):
    queryset = models.Pokemon.objects.all()
    serializer_class = serializers.PokemonSerializer