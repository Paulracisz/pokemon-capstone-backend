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
            if len(response['abilities']) == 3 and len(response['types']) == 2:

                Pokemon.objects.create(
                    name=response['name'],
                    front_normal_image=response['sprites']['front_default'],
                    front_shiny_image=response['sprites']['front_shiny'],
                    hp=response['stats'][0]['base_stat'],
                    attack=response['stats'][1]['base_stat'],
                    defense=response['stats'][2]['base_stat'],
                    special_attack=response['stats'][3]['base_stat'],
                    special_defense=response['stats'][4]['base_stat'],
                    speed=response['stats'][5]['base_stat'],
                    ability_One=response['abilities'][0]['ability']['name'],
                    ability_Two=response['abilities'][1]['ability']['name'],
                    ability_Three=response['abilities'][2]['ability']['name'],
                    type_One=response['types'][0]['type']['name'],
                    type_Two=response['types'][1]['type']['name'],
                    base_experience=response['base_experience']
                )

            elif len(response['abilities']) == 3:

                Pokemon.objects.create(
                    name=response['name'],
                    front_normal_image=response['sprites']['front_default'],
                    front_shiny_image=response['sprites']['front_shiny'],
                    hp=response['stats'][0]['base_stat'],
                    attack=response['stats'][1]['base_stat'],
                    defense=response['stats'][2]['base_stat'],
                    special_attack=response['stats'][3]['base_stat'],
                    special_defense=response['stats'][4]['base_stat'],
                    speed=response['stats'][5]['base_stat'],
                    ability_One=response['abilities'][0]['ability']['name'],
                    ability_Two=response['abilities'][1]['ability']['name'],
                    ability_Three=response['abilities'][2]['ability']['name'],
                    type_One=response['types'][0]['type']['name'],
                    type_Two="N/A",
                    base_experience=response['base_experience']
                )

            elif len(response['abilities']) == 2 and len(response['types']) == 2:

                Pokemon.objects.create(
                    name=response['name'],
                    front_normal_image=response['sprites']['front_default'],
                    front_shiny_image=response['sprites']['front_shiny'],
                    hp=response['stats'][0]['base_stat'],
                    attack=response['stats'][1]['base_stat'],
                    defense=response['stats'][2]['base_stat'],
                    special_attack=response['stats'][3]['base_stat'],
                    special_defense=response['stats'][4]['base_stat'],
                    speed=response['stats'][5]['base_stat'],
                    ability_One=response['abilities'][0]['ability']['name'],
                    ability_Two=response['abilities'][1]['ability']['name'],
                    ability_Three="N/A",
                    type_One=response['types'][0]['type']['name'],
                    type_Two=response['types'][1]['type']['name'],
                    base_experience=response['base_experience']
                )

            elif len(response['abilities']) == 2:

                Pokemon.objects.create(
                    name=response['name'],
                    front_normal_image=response['sprites']['front_default'],
                    front_shiny_image=response['sprites']['front_shiny'],
                    hp=response['stats'][0]['base_stat'],
                    attack=response['stats'][1]['base_stat'],
                    defense=response['stats'][2]['base_stat'],
                    special_attack=response['stats'][3]['base_stat'],
                    special_defense=response['stats'][4]['base_stat'],
                    speed=response['stats'][5]['base_stat'],
                    ability_One=response['abilities'][0]['ability']['name'],
                    ability_Two=response['abilities'][1]['ability']['name'],
                    ability_Three="N/A",
                    type_One=response['types'][0]['type']['name'],
                    type_Two="N/A",
                    base_experience=response['base_experience']
                )

            elif len(response['abilities']) == 1 and len(response['types']) == 2: 

                Pokemon.objects.create(
                    name=response['name'],
                    front_normal_image=response['sprites']['front_default'],
                    front_shiny_image=response['sprites']['front_shiny'],
                    hp=response['stats'][0]['base_stat'],
                    attack=response['stats'][1]['base_stat'],
                    defense=response['stats'][2]['base_stat'],
                    special_attack=response['stats'][3]['base_stat'],
                    special_defense=response['stats'][4]['base_stat'],
                    speed=response['stats'][5]['base_stat'],
                    ability_One=response['abilities'][0]['ability']['name'],
                    ability_Two="N/A",
                    ability_Three="N/A",
                    type_One=response['types'][0]['type']['name'],
                    type_Two=response['types'][1]['type']['name'],
                    base_experience=response['base_experience']
                )

            else:

                Pokemon.objects.create(
                    name=response['name'],
                    front_normal_image=response['sprites']['front_default'],
                    front_shiny_image=response['sprites']['front_shiny'],
                    hp=response['stats'][0]['base_stat'],
                    attack=response['stats'][1]['base_stat'],
                    defense=response['stats'][2]['base_stat'],
                    special_attack=response['stats'][3]['base_stat'],
                    special_defense=response['stats'][4]['base_stat'],
                    speed=response['stats'][5]['base_stat'],
                    ability_One=response['abilities'][0]['ability']['name'],
                    ability_Two="N/A",
                    ability_Three="N/A",
                    type_One=response['types'][0]['type']['name'],
                    type_Two="N/A",
                    base_experience=response['base_experience']
                )
