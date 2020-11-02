from django.shortcuts import render

import random

# Create your views here.

def home(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    if request.GET.get('symbols'):
        characters.extend(list('!@#$%^&*()_-+=|'))

    length = int(request.GET.get('length', 10)) # if the length was set will be length otherwise the length will be 10.
    password = ""
    for x in range(length):
        password += random.choice(characters)

    context = {
        'password': password
    }
    return render(request, 'generator/home.html', context)