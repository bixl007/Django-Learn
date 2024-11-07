from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello, You are at Home page")
    return render(request, 'website/index.html')

def about(request):
    return HttpResponse("Hello, You are at About page")

def contact(request):
    return HttpResponse("Hello, You are at Contact page")