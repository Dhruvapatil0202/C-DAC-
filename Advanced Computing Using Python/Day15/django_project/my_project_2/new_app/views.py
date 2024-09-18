from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'new_app/home.html')

def another_page(request):
    return render(request, 'new_app/another_page.html')

