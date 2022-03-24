from django.shortcuts import render
from random import randint, random
from .models import Kerdes # a mostani konyvtarban levo models

# Create your views here.

def index (request):
    print(request.POST)
    if request == 'POST':
        kerdesnev = request.POST['kedvencszo']
        Kerdes.objects.create(kerdes=kerdesnev)

    template = "index.html"
    context = {'kerdesek': Kerdes.objects.all()}
    return render(request, template, context)
