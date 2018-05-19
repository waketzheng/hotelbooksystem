from django.contrib import admin

from .models import Hotel, Customer, RoomInfo, Order, Poster


admin.site.register(Hotel)
admin.site.register(Customer)
admin.site.register(RoomInfo)
admin.site.register(Order)
admin.site.register(Poster)
