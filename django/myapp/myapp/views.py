from django.http import HttpResponse
from django.shortcuts import render


def test(request):
   print("test function called")
   return HttpResponse(" <h1>Hello Django Test</h1>")

def about(request):
   return render(request,"about.html",{})

def contact(request):
   return render(request,"contact.html",{})

def home(request):
   return render(request,"home.html",{})