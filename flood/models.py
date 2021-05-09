from django.db import models

# Create your models here.
from django.db import models


class Person(models.Model):
    email = models.CharField(max_length=30)
    pincode = models.CharField(max_length=10)