from django.shortcuts import render

# Create your views here.

# myapp/views.py
from django.http import HttpResponse

def home(request):
    return render(request, 'myapp/home.html')
    # return HttpResponse('Hello, Django!')

def about(request):
    return render(request, 'myapp/about.html')
    # return HttpResponse('This is the About Page!') # New screen

