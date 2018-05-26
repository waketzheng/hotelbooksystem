from django.contrib import admin

from .models import Hotel, Customer, Room, Order, Poster


admin.site.register(Hotel)
admin.site.register(Customer)
admin.site.register(Room)
admin.site.register(Order)
admin.site.register(Poster)
