from django.db import models
from django.conf import settings

# Create your models here.


class Contact(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=32)
    message = models.TextField()

    def __str__(self):
        return self.email


class Events(models.Model):
    purpose = models.CharField(max_length=60)
    date = models.DateTimeField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.purpose


class News(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateTimeField()
    text = models.TextField()

    def __str__(self):
        return self.title


class Sermon(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)

    title = models.CharField(max_length=100)
    date = models.DateTimeField()
