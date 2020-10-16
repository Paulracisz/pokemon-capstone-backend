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

class PokemonTrainerList(APIView):
    """
    Create a new user. It's called 'PokemonTrainerList' because normally we'd have a get
    method here too, for retrieving a list of all User objects.
    """

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = serializers.PokemonTrainerSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PokemonTrainerViewSet(viewsets.ModelViewSet):
    queryset = models.PokemonTrainer.objects.all()
    serializer_class = serializers.PokemonTrainerSerializer
    
class PokemonViewSet(viewsets.ModelViewSet):
    queryset = models.Pokemon.objects.all()
    serializer_class = serializers.PokemonSerializer
    
    
class CaughtPokemonViewSet(viewsets.ModelViewSet):
    queryset = models.CaughtPokemon.objects.all()
    serializer_class = serializers.CaughtPokemonSerializer