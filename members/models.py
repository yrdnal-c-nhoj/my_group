from django.db import models


class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)
  joined_date = models.DateField(null=True)
  
  #  this is changing my information into strings 
  # Defining our own __str__() function is not a Django feature, 
  # it is how to change the string representation of objects in Python. 
#either do this or change it in the admin file

#  def __str__(self):
 #   return f"{self.firstname} {self.lastname}"