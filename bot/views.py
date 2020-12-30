from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    #ok
    print('hello1')

    return HttpResponse('200')
