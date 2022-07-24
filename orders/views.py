from datetime import datetime
from random import choice

from django.shortcuts import render

from houses.models import Hotel

from .models import Customer, Order, RoomType


def order(request):
    hotel = Hotel.objects.first()
    # TODO: check whether rooms are avalible
    return render(request, "order.html", {"hotel": hotel})


def order_done(request):
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
