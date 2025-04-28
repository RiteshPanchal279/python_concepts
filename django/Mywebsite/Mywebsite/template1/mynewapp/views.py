from django.shortcuts import render

from Mywebsite.template1.mynewapp.models import User

# Create your views here.
def registratin(request):
   return render(request,'mynewapp/registration.html',{})


def insertuser(request):
   vuid=request.post['uid']
   vuname=request.post['uname']
   vemail=request.post['email']
   vcontact=request.post['contact']

   us = User(uid=vuid,uname=vuname,email=vemail,contact=vcontact)
   us.save()
   return render(request,'mynewapp/registration.html',{})