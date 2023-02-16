from django.contrib import admin
from django.urls import path
from asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', HomeView.as_view()),
    path('', LoginView.as_view()),
    path('register/', register),
    path('logout/', logoutview),
    path('todo_ochir/<int:son>/', Todo_ochirView.as_view()),
    path('todo_edit/<int:son>/', Todo_editView.as_view()),
]
