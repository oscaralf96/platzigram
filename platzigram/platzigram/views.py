"""Platzigram views."""

# Django
import json

from django.http import HttpResponse,JsonResponse

#Utilities
from datetime import datetime

def hello_world(request):
    """Return a greeting"""
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse(f'Hi, la fecha del servidor es {now}')


def sorted(request):
    """Hi."""
    # para la ejecucion del programa hasta que le demos 'c': continuar
    #import pdb; pdb.set_trace()
    numbers = [int(num) for num in request.GET['numbers'].split(',')]
    numbers.sort()
    print(numbers)
    data = {
        'status': 'ok',
        'numbers': numbers
    }

    #return JsonResponse(json.dumps(data, indent=4), safe=False)
    return JsonResponse(json.dumps(data))
    #return HttpResponse(str(numbers), content_type='application/json')

def say_hi(request, name, age):
    """Return greeting"""
    if age < 12:
        message = f'Sorry {name}, you are under 18'
    else:
        message = f'Welcome, {name}!'

    return HttpResponse(message)