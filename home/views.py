from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("HomePage")

def about(request):
    return HttpResponse("about")

def project(request):
    return HttpResponse("project")

def contact(request):
    return HttpResponse("contact")
