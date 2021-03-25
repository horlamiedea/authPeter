from django.core import paginator
from django.db import models
from django.db.models.base import Model
from django.shortcuts import render
from django.contrib import messages
from django.views.generic import View
from .models import Contact, Events
from django.core.paginator import Paginator

# Create your views here.


class Home(View):

    def get(self, *args, **kwargs):
        events = Events.objects.all()
        paginator = Paginator(events, 5)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        # context = {
        #     'events': events
        # }
        return render(self.request, 'index.html', {'page_obj': page_obj})

    def post(self, *args, **kwargs):
        form = Contact(self.request.POST)
        if self.request.method == 'POST':
            name_r = self.request.POST.get('name')
            email_r = self.request.POST.get('email')
            message_r = self.request.POST.get('message')

        c = Contact(name=name_r, email=email_r, message=message_r)
        c.save()
        return render(self.request, 'index.html')
