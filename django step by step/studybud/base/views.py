from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.

rooms = [
    {'id': 1, 'name': 'Lets Learn Python'},
    {'id': 2, 'name': 'Lets Learn java'},
    {'id': 3, 'name': 'Lets Learn React JS'},
]


def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request, pk):
    return render(request, 'base/room.html')
