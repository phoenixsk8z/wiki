from django.shortcuts import render
from django.http import HttpResponse

def index2(request):
    return HttpResponse("Hello, World!")


def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")
