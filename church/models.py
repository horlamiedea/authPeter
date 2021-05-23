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
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
