from django.http import HttpResponse

def test(request):
   print("test function called")
   return HttpResponse(" <h1>Hello Django</h1>")