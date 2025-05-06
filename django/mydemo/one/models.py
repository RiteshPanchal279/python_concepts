from django.db import models

# Create your models here.
class Employee(models.Model):
   eid = models.AutoField(primary_key=True)
   ename = models.CharField(max_length=20)
   eemail = models.CharField(max_length=20)
   ecity = models.CharField(max_length=20)
   
   class Meta:
      db_table="employee"
