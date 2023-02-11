from django.contrib import admin
from django.urls import path
from asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('todo_ochir/<int:son>/', todo_ochirish),
]
