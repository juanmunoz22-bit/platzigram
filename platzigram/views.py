#Platzigram views

#Django
import pdb
from django.http import HttpResponse

#Utilities
from datetime import datetime
import json

def hello_world(request):
    #Return hello world
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Oh hi! Current server time is {}'.format(now))

def sort_integers(request):
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    data = {
        'numbers': sorted_ints,
        'status': 'ok',
        'message': 'Integers sorted succesfully'
    }

    return HttpResponse(json.dumps(data, indent=4), content_type='application/json')

def say_hi(request, name, age):
    if age < 12:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hello {}, welcome to Platzigram'.format(name)
    return HttpResponse(message)