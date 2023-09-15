from rest_framework.decorators import api_view
from rest_framework.response import Response
from math import floor
from random import random

BOOKSTORE = [
    {'title': 'My Brilliant Friend', 'author': 'Elena Ferrante'},
    {'title': 'Piranesi', 'author': 'Susanna Clarke'},
    {'title': 'The Summer Book', 'author': 'Tove Jansson'},
    {'title': 'Middlemarch', 'author': 'George Eliot'},
    {'title': 'Song of Solomon', 'author': 'Toni Morrison'},
    {'title': 'The Tale of Genji', 'author': 'Lady Murasaki'},
]

def get_random_int(range):
    return floor(random() * range)

@api_view(['GET'])
def randomize_book(request):
    range = len(BOOKSTORE)
    rng = get_random_int(range)
    return Response(BOOKSTORE[rng])
