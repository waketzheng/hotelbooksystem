from datetime import datetime
from random import choice
from django.conf import settings
from django.http import Http404
from django.shortcuts import render
from .models import Hotel, Room, RoomType, Order, Customer


def index(request):
    # TODO: bind hotel name by Site
    hotel = Hotel.objects.first()
    if not hotel:
        raise Http404("No hotel yet.")
    return render(request, "index.html", {"hotel": hotel})


def room_info(request):
    hotel = Hotel.objects.first()
    roomtypes = RoomType.objects.filter(hotel=hotel)
    return render(
        request, "roominfo.html", {"roomtypes": roomtypes, "hotel": hotel}
    )


def order(request):
    hotel = Hotel.objects.first()
    # TODO: check whether rooms are avalible
    return render(request, "order.html", {"hotel": hotel})


def order_done(request):
    print(request.POST)
    customer, created = Customer.objects.get_or_create(
        phone=request.POST["phone"],
        name=request.POST["name"],
        id_card=request.POST["IDcard"],
    )
    begin, end = request.POST["begin"], request.POST["end"]
    begin = datetime.strptime(begin, "%Y-%m-%d").date()
    end = datetime.strptime(end, "%Y-%m-%d").date()
    period = (end - begin).days or 1
    roomtype = RoomType.objects.get(detail=request.POST["roomtype"])
    order = Order.objects.create(
        customer=customer,
        roomtype=roomtype,
        begin=begin,
        end=end,
        room=choice(roomtype.room_set.all()),
        totalprice=period * roomtype.price,
    )
    return render(request, "done_order.html", {"order": order})


def about(request):
    hotel = Hotel.objects.first()
    return render(request, "about.html", {"hotel": hotel})
