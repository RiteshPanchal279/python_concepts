from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
   return HttpResponse("<h1> MY Second app -> Home 2 </h1>")

def contact(request):
   return HttpResponse("<h1> MY Second app --> contact 2 </h1>")

