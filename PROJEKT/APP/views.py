from django.shortcuts import render
from random import randint, random
from .models import Kerdes # a mostani konyvtarban levo models

# Create your views here.

def bigyoview (request):
    kerdesek = Kerdes.objects.all()

    for kerdes in kerdesek:
        print(kerdes)

    template = "bigyotemplate.html"
    context = {'a' : randint(0, 10), 'kerdesek2': kerdesek}
    return render(request, template, context)
