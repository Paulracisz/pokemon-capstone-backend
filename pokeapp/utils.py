from mainapp.serializers import PokemonTrainerSerializer


def my_jwt_response_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': PokemonTrainerSerializer(user, context={'request': request}).data
    }