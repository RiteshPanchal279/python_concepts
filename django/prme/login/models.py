from django.db import models

# Create your models here.
class Login(models.Model):
   
   email = models.CharField(max_length=50)
   pswd = models.CharField(max_length=50)
   
   class Meta:
      db_table = "login"