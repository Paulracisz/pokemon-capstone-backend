from django.contrib import admin
from mainapp.models import PokemonTrainer, Pokemon
from django.contrib.auth.admin import UserAdmin

class PokemonTrainerAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Pokemon Trainer',
            {
                'fields': (
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
                ),
            },
        ),
    )

# Register your models here.

admin.site.register(PokemonTrainer, PokemonTrainerAdmin)
admin.site.register(Pokemon)
