from django.db import models
from datetime import datetime,date
# Create your models here.
class CreateLogin(models.Model):
     first_name=models.CharField(max_length=30)
     last_name=models.CharField(max_length=30)
     address=models.CharField(max_length=300)
     Gender=models.CharField(max_length=1)
     State=models.CharField(max_length=20)
     City=models.CharField(max_length=30)
     Dob=models.DateField(auto_now_add=False,auto_now=False,blank=True)
     Pincode= models.IntegerField(blank=True, null=True)
     Course=models.CharField(max_length=30)
     Email=models.CharField(max_length=50)
     
     