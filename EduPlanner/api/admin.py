from django.contrib import admin
from .models import User, Event, Holiday, Notification, Review

admin.site.register(User)
admin.site.register(Event)
admin.site.register(Holiday)
admin.site.register(Notification)
admin.site.register(Review)
