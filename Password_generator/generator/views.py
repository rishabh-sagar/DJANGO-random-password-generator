from django.shortcuts import render
from django.http import HttpResponse
import random


def password(request):
    char = list('')
    chars = list('qwertyuiopasdfghjklzxcvbnm')
    num = list('0123456798')
    upperchar = list('QWERTYUIOPASDFGHJKLZXCVBNM')
    special = list('''!@#%^&*()_+=-{}][}{":.,<>?''')

    length = int(request.GET.get('l', 10))

    if(request.GET.get('uppercase')):
        char.extend(upperchar)

    if (request.GET.get('numbers')):
        char.extend(num)

    if (request.GET.get('specialcharacter')):
        char.extend(special)

    else:
        char.extend(chars)
        char.extend(num)
        char.extend(special)

    password = ''

    for x in range(length):
        password += random.choice(char)

    hi = {
        'password': password

    }
    return render(request, 'generator/password.html', hi)


def index(request):

    return render(request, 'generator/index.html')
