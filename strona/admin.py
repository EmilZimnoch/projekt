from django.contrib import admin
from .models import Service, Room, Smart, TypeOfSpot, Spot
# Register your models here.
admin.site.register(Service)
admin.site.register(Room)
admin.site.register(Smart)
admin.site.register(TypeOfSpot)
#admin.site.register(Furrowing)
admin.site.register(Spot)
