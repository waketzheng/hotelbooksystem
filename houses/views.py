from django.http import Http404
from django.shortcuts import render

from .models import Hotel, RoomType


def index(request):
    # to be extend: bind hotel name by Site
    hotel = Hotel.objects.first()
    if not hotel:
        raise Http404("No hotel yet.")
    return render(request, "index.html", {"hotel": hotel})


def room_info(request):
    hotel = Hotel.objects.first()
    roomtypes = RoomType.objects.filter(hotel=hotel)
    context = {"roomtypes": roomtypes, "hotel": hotel}
    return render(request, "roominfo.html", context)


def about(request):
    hotel = Hotel.objects.first()
    return render(request, "about.html", {"hotel": hotel})
