from django.core.management.base import BaseCommand, CommandError
from mainapp.models import Pokemon
import requests

pokemon_names = []


def get_pokemon():
    main_api_header = "https://pokeapi.co/api/v2/"
    gen_one_pokemon = f"{main_api_header}generation/1"
    pokemon_r = requests.get(gen_one_pokemon).json()
    pokemon = pokemon_r['pokemon_species']
    for pokemon in pokemon:
        pokemon_names.append(pokemon['name'])


get_pokemon()


class Command(BaseCommand):

    def handle(self, *args, **options):

        main_api_header = "https://pokeapi.co/api/v2/"
        specific_pokemon = f"{main_api_header}pokemon/"

        for name in pokemon_names:
            pokemon_stats = f"{specific_pokemon}{name}"
            response = requests.get(pokemon_stats).json()
            Pokemon.objects.create(
                name= f"{response}{['name']}",
                hp = response['stats'][0]['base_stat'],
                attack = response['stats'][1]['base_stat'],
                defense = response['stats'][2]['base_stat'],
                speed = response['stats'][5]['base_stat'],
                special_attack = response['stats'][3]['base_stat'],
                special_defense = response['stats'][4]['base_stat'],
                ability_One = f"{response}{['abilities']}{[0]}{['ability']}{['name']}",
                ability_Two = f"{response}{['abilities']}{[1]}{['ability']}{['name']}",
                type_One = f"{response}{['types']}{[0]}{['type']}{['name']}",
                type_Two = f"{response}{['types']}{[1]}{['type']}{['name']}",
                front_normal_image = f"{response}{['sprites']}{['front_default']}",
                front_shiny_image = f"{response}{['sprites']}{['front_shiny']}",
                base_experience = response['base_experience'],
            )
