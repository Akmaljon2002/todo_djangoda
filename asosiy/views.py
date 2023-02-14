from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import *

def home(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form =KundalikForm(request.POST)
            if form.is_valid():
                plan = form.save(commit=False)
                plan.foydalanuvchi = request.user
                plan.save()
            return redirect("/todo/")
        data = {
            "kundaliklar":Kundalik.objects.filter(foydalanuvchi=request.user),
            "kundalik":KundalikForm()
        }
        return render(request, 'todo.html', data)
    return redirect("/")

def todo_ochirish(request, son):
    todo = Kundalik.objects.get(id=son)
    todo.delete()

    return redirect("/")

# 1
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

def loginview(request):
    if request.method == "POST":
        user = authenticate(username=request.POST.get('l'),
                     password=request.POST.get('p'))
        if user is None:
            return redirect("/")
        login(request, user)
        return redirect("/todo/")
    return render(request, 'login.html')


def logoutview(request):
    logout(request)
    return redirect("/")
