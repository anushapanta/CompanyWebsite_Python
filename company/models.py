from django.db import models

# Create your models here.
class Contactus(models.Model):
    fullname = models.CharField(max_length=60, unique=True)
    email = models.CharField(max_length=60, unique=True)
    description = models.TextField(max_length=400)
    date = models.DateTimeField(auto_now_add=True)



