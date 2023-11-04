from django.shortcuts import render, HttpResponse
from .models import ToDoList

# Create your views here.

def home(request):
    return render(request, "home.html")

def todos(request):
    items = ToDoList.objects.all()
    return render(request, 'todolist.html',{'todos': items})