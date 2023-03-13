from django.shortcuts import render
import requests
import json
import pprint

pp = pprint.PrettyPrinter(indent=2, depth=2)

def index(request):
    return render(request, 'pages/pokemon_form.html')

def get_pokemon(request):
    item_title = request.GET.get('user_input')
    endpoint = f'https://pokeapi.co/api/v2/pokemon/{item_title}'
    response = requests.get(endpoint)
    response_json = json.loads(response.content)
    pokemon_name = response_json['name']
    pokemon_img = response_json['sprites']['front_default']
    pp.pprint(response_json['types'][0]['type']['name'])
    
    data = {
        'name': pokemon_name,
        'img': pokemon_img
    }
    
    return render(request, 'pages/get_pokemon.html', data)