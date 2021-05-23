from django.urls import path
from .views import Home, Event, Sermonss

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path("event", Event.as_view(), name="event"),
    path("sermons", Sermonss.as_view(), name="sermon")
]
