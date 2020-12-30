from django.shortcuts import render

# Create your views here.
def index(request):
    print('hello1')
    return HttpResponse('200')
