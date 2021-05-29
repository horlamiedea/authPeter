from django.contrib import admin
from .models import Contact, Events, News, Sermon, FirstTimer

# Register your models here.
admin.site.register(Contact)
admin.site.register(Events)
admin.site.register(News)
admin.site.register(Sermon)
admin.site.register(FirstTimer)
