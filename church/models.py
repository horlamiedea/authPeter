from django.db import models

# Create your models here.


class Contact(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=32)
    message = models.TextField()


class Events(models.Model):
    purpose = models.CharField(max_length=60)
    date = models.DateTimeField()
    location = models.CharField(max_length=100)
