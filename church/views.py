from django.core import paginator
from django.db import models
from django.db.models.base import Model
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import View, ListView
from .models import Contact, Events, News, Sermon, FirstTimer
from django.core.paginator import Paginator

# Create your views here.


class Home(View):

    def get(self, *args, **kwargs):
        events = Events.objects.all()
        paginator = Paginator(events, 5)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        news = News.objects.all()
        pag = Paginator(news, 4)
        pag_num = self.request.GET.get('page')
        pag_obj = pag.get_page(pag_num)
        sermon = Sermon.objects.all()
        pags = Paginator(sermon, 3)
        pags_num = self.request.GET.get('page')
        pags_obj = pags.get_page(pags_num)
        context = {
            'page_obj': page_obj,
            'pag_obj': pag_obj,
            'pags_obj': pags_obj
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


def event(request):
    return render(request, 'event.html')


class Event(ListView):
    model = Events
    paginate_by = 4
    template_name = 'event.html'


class Sermonss(ListView):
    model = Sermon
    paginate_by = 4
    template_name = 'sermon.html'


class VisitorView(View):
    def get(self, *args, **kwargs):
        return render(self.request, 'visitors.html')

    def post(self, *args, **kwargs):
        if self.request.method == 'POST':
            name = self.request.POST.get('first_name')
            name_r = self.request.POST.get('last_name')
            email = self.request.POST.get('email')
            phone = self.request.POST.get('phone_number')
            address = self.request.POST.get('address')
            city = self.request.POST.get('city')
            state = self.request.POST.get('state')
            about = self.request.POST.get('about_you')

            collect = FirstTimer()
            collect.first_name = name
            collect.last_name = name_r
            collect.email = email
            collect.phone_number = phone
            collect.address = address
            collect.city = city
            collect.state = state
            collect.about_you = about
            collect.save()

            messages.success(
                self.request, f"Welcome to Our Church {name} {name_r}. We have appointed a host to you, The host will get accross to you very soon")
            return redirect('home')
