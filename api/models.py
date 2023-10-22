from typing import Any
from django.db import models

# Create your models here.
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(max_length=100,choices=(('IT','IT'),
                                                    ('Non IT','Non IT'),
                                                    ('Mobile Phones','Mobile Phones')))
    
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    #this is for showing the connection (company) name in the api table or json instead of ID 
    def __str__(self):
        return self.name + self.location
 

# Employee model
class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    email = models.CharField(max_length=60)
    name = models.CharField(max_length=60)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=11)
    about = models.TextField()
    position = models.CharField(max_length=100,choices=(('Manager','manager'),
                                                    ('Software Developer','Sd'),
                                                    ('Project Leader','Pl')))