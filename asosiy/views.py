from django.shortcuts import render, redirect
from .models import *
from .forms import *

def home(request):
    if request.method == "POST":
        form =KundalikForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    data = {
        "kundaliklar":Kundalik.objects.all(),
        "kundalik":KundalikForm()
    }
    return render(request, 'todo.html', data)

def todo_ochirish(request, son):
    todo = Kundalik.objects.get(id=son)
    todo.delete()

    return redirect("/")

