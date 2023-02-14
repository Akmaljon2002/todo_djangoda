from django.contrib import admin
from django.urls import path
from asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', home),
    path('', loginview),
    path('logout/', logoutview),
    path('todo_ochir/<int:son>/', todo_ochirish),
    path('todo_edit/<int:son>/', todo_edit),
]
