from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    response = 'The GITHUB AWS Pipeline works fine. Deployed on 19.12.2022'
    return HttpResponse(response)
