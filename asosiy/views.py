from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import *

class HomeView(View):
    def post(self, request):
        form = KundalikForm(request.POST)
        if form.is_valid():
            plan = form.save(commit=False)
            plan.foydalanuvchi = request.user
            plan.save()
        return redirect("/todo/")
    def get(self, request):
        if request.user.is_authenticated:
            data = {
                "kundaliklar":Kundalik.objects.filter(foydalanuvchi=request.user),
                "kundalik":KundalikForm()
            }
            return render(request, 'todo.html', data)
        return redirect("/")

class Todo_ochirView(View):
    def get(self, request, son):
        if request.user.is_authenticated:
            todo = Kundalik.objects.get(id=son)
            if todo.foydalanuvchi == request.user:
                todo.delete()
            return redirect("/todo/")

        return redirect("/")


# 1
class Todo_editView(View):
    def get(self, request, son):
        if request.user.is_authenticated:
            data = {
                "todo": Kundalik.objects.get(id=son),
                "st": ["Boshlanadi", "Boshlandi", "Bajarildi"]
            }
            return render(request, "todo_edit.html", data)
        return redirect("/todo/")

    def post(self, request, son):
        Kundalik.objects.filter(id=son).update(
            sarlavha = request.POST.get('s'),
            muddat = request.POST.get('m'),
            batafsil = request.POST.get('b'),
            status = request.POST.get('status')
        )
        return redirect("/")


class LoginView(View):
    def post(self, request):
        user = authenticate(username=request.POST.get('l'),
                            password=request.POST.get('p'))
        if user is None:
            return redirect("/")
        login(request, user)
        return redirect("/todo/")
    def get(self, request):
        return render(request, 'login.html')



class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("/")

def register(request):
    if request.method == "POST" and request.POST.get('p') == request.POST.get('cp'):
        User.objects.create_user(
            username = request.POST.get('l'),
            password = request.POST.get('p')
        )
        return redirect("/")
    return render(request, 'register.html')
