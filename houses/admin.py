from django.contrib import admin

from .models import Hotel, Poster, Room, RoomType

admin.site.register(Hotel)
admin.site.register(RoomType)
admin.site.register(Room)
admin.site.register(Poster)
