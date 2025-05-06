from django.shortcuts import redirect, render
from .models import Employee

def welcome(request):
   data={}
   if request.method=="POST":
      e1 = request.POST['ename']
      e2 = request.POST['eemail']
      e3 = request.POST['ecity']
      obj = Employee(ename=e1,eemail=e2,ecity=e3)
      obj.save()
   
   data['record']=Employee.objects.all()
   return render(request,"welcome.html",data)


def emp_edit(request,id):
   data={}
   if request.method=="POST":
      e1 = request.POST['ename']
      e2 = request.POST['eemail']
      e3 = request.POST['ecity']
      obj = Employee.objects.get(eid=id)
      obj.ename=e1
      obj.eemail=e2
      obj.ecity=e3
      obj.save()
   data["record"] = Employee.objects.get(eid=id)
   return render(request,'Employee.html',data)

def emp_delete(request,id):
   Employee.objects.get(eid=id).delete()
   return redirect(welcome)