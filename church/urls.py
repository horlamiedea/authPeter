from django.urls import path
from .views import Home, Event

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path("event", Event.as_view(), name="event")
]
