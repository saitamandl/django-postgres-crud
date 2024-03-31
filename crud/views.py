from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the Crud Index")

def say_hello(request):
    return render(request, 'hello.html')