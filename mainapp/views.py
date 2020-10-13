from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from mainapp import serializers, models

# Create your views here.

@api_view(['GET'])
def current_trainer(request):
    """
    Determine the current trainer by their token, and return their data
    """
    serializer = serializers.PokemonTrainerSerializer(request.user)
    return Response(serializer.data)


class PokemonTrainerViewSet(viewsets.ModelViewSet):
    queryset = models.PokemonTrainer.objects.all()
    serializer_class = serializers.PokemonTrainerSerializer
    
class PokemonViewSet(viewsets.ModelViewSet):
    queryset = models.Pokemon.objects.all()
    serializer_class = serializers.PokemonSerializer