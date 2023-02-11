from django.shortcuts import render
from .models import *

def home(request):
    data = {
        "kundalik":Kundalik.objects.all()
    }
    return render(request, 'todo.html', data)