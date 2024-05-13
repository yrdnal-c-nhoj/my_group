from django.db import models


class Animal(models.Model):
    animalname = models.CharField(max_length=255)
    latinname = models.CharField(max_length=255)
    population = models.IntegerField(null=True)
    characteristics = models.CharField(max_length=255)
    #  this is changing my information into strings 
    # Defining our own __str__() function is not a Django feature, 
    # it is how to change the string representation of objects in Python. 
    #either do this or change it in the admin file

#  def __str__(self):
 #   return f"{self.firstname} {self.lastname}"