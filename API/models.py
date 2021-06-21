from django.db import models

# Create your models here.

class animal(models.Model):
    name = models.CharField(max_length = 200)
    age = models.CharField(max_length = 5)
    specie = models.CharField(max_length = 100)
    weight = models.CharField(max_length = 10)
    blood_type = models.CharField(max_length = 10)