from django.contrib import admin
from .models import User, PlaceUser, ActionPlace
# Register your models here.

admin.site.register(User)
admin.site.register(PlaceUser)
admin.site.register(ActionPlace)
