from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
   return HttpResponse("<h1> MY first app -> Home </h1>")

def contact(request):
   return HttpResponse("<h1> MY first app --> contact </h1>")




