from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse

# Create your models here.


class Contact(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=32)
    message = models.TextField()

    def __str__(self):
        return self.email


class Events(models.Model):
    purpose = models.CharField(max_length=60)
    date = models.DateTimeField(default=timezone.now)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.purpose

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class News(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateTimeField(default=timezone.now)
    text = models.TextField()

    def __str__(self):
        return self.title


class Sermon(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)

    title = models.CharField(max_length=100)
    text = models.TextField(blank=True, null=True)
    mp3 = models.FileField(blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class FirstTimer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=100)
    about_you = models.TextField()

    def __str__(self):
        return f"{self.first_name } {self.last_name}"
