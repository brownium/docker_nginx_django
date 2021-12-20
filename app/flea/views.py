from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def flea(requests):
    return HttpResponse("flea")