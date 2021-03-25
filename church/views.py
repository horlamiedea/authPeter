from django.db import models
from django.db.models.base import Model
from django.shortcuts import render
from django.contrib import messages
from django.views.generic import View
from .models import Contact, Events

# Create your views here.


class Home(View):

    def get(self, *args, **kwargs):
        events = Events.objects.all()
        context = {
            'events': events
        }
        return render(self.request, 'index.html', context)

    def post(self, *args, **kwargs):
        form = Contact(self.request.POST)
        if self.request.method == 'POST':
            name_r = self.request.POST.get('name')
            email_r = self.request.POST.get('email')
            message_r = self.request.POST.get('message')

        c = Contact(name=name_r, email=email_r, message=message_r)
        c.save()
        return render(self.request, 'index.html')
