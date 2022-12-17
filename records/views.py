from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    response = 'The GITHUB AWS Pipeline works fine'
    return HttpResponse(response)
