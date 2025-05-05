from django.db import models

# Create your models here.
class Signup(models.Model):
    
   name = models.CharField(max_length=50)  
   email = models.CharField(max_length=50)
   pswd = models.CharField(max_length=50)
   address = models.CharField(max_length=50)
   
   class Meta:
      db_table = "signup"