from django.db import models

# Create your models here.
class User(models.Model):
   uid = models.CharField(max_length=20)
   uname = models.CharField(max_length=20)
   email = models.EmailField()
   contact = models.CharField(max_length=20)

   class Meta:
      db_table="User"