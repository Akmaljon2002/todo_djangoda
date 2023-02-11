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

def todo_edit(request, son):
    if request.method == "POST":
        Kundalik.objects.filter(id=son).update(
            sarlavha = request.POST.get('s'),
            muddat = request.POST.get('m'),
            batafsil = request.POST.get('b'),
            status = request.POST.get('status')
        )
        return redirect("/")
    data = {
        "todo":Kundalik.objects.get(id=son),
        "st":["Boshlanadi", "Boshlandi", "Bajarildi"]
    }
    return render(request, "todo_edit.html", data)
