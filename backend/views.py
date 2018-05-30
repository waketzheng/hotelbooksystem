import datetime
from random import randint
from django.conf import settings
from django.http import Http404
from django.shortcuts import render
from .models import Hotel, Room, Order, Customer


def index(request):
    # TODO: bind hotel name by Site
    hotel = Hotel.objects.first()
    if not hotel:
        raise Http404("No hotel yet.")
    return render(request, "index.html", {"hotel": hotel})


def room_info(request):
    rooms = Room.objects.all()
    imgObjs = ImageAtQiniu.objects.all()
    imgUrls = [QiniuPush.private_download_url(i.fullname) for i in imgObjs]
    imgs = ImgList()

    for i in imgUrls:
        if "hotel-logo" in i:
            imgs.logo = i

    return render(request, "roominfo.html", {"rooms": rooms, "img": imgs})


def order(request):
    # TODO: without qiniu
    imgObjs = ImageAtQiniu.objects.all()
    imgUrls = [QiniuPush.private_download_url(i.fullname) for i in imgObjs]
    imgs = ImgList()

    for i in imgUrls:
        if "hotel-logo" in i:
            imgs.logo = i

    return render(request, "order.html", {"img": imgs})


def order_done(request):
    imgObjs = ImageAtQiniu.objects.all()
    imgUrls = [QiniuPush.private_download_url(i.fullname) for i in imgObjs]
    imgs = ImgList()

    for i in imgUrls:
        if "hotel-logo" in i:
            imgs.logo = i

    tel, name = request.GET["tel"], request.GET["name"]
    IDcard = request.GET["IDcard"]
    if Customer.objects.all():
        cc = Customer.objects.filter(IDcard=IDcard)
    else:
        cc = []
    for c in cc:
        if c and c.tel == tel and c.name == name:
            tempCustomer = c
            break
    else:
        tempCustomer = Customer(tel=tel, name=name, IDcard=IDcard)
        tempCustomer.save()

    tempOrder = Order()
    tempOrder.customer = tempCustomer
    tempOrder.roomtype = request.GET["roomtype"]

    begin, end = request.GET["begin"], request.GET["end"]
    tempOrder.begin = (datetime.datetime.strptime(begin, "%Y-%m-%d")).date()
    tempOrder.end = (datetime.datetime.strptime(end, "%Y-%m-%d")).date()
    period = (tempOrder.end - tempOrder.begin).days
    if period == 0:
        period = 1

    price = 0

    if tempOrder.roomtype == "standard":
        price = (Room.objects.get(name="标准间")).price

    elif tempOrder.roomtype == "better":
        price = (Room.objects.get(name="豪华间")).price

    elif tempOrder.roomtype == "president":
        price = (Room.objects.get(name="总统间")).price

    tempOrder.roomnum = randint(1, 10)
    tempOrder.totalprice = period * price
    tempOrder.save()

    return render(
        request, "orderresult.html", {"order": tempOrder, "img": imgs}
    )


def about(request):
    title = "DJango Hotel"
    hotel = Hotel.objects.first()
    name = hotel.name
    summary = hotel.summary
    address = hotel.address

    imgObjs = ImageAtQiniu.objects.all()
    imgUrls = [QiniuPush.private_download_url(i.fullname) for i in imgObjs]
    imgs = ImgList()

    for i in imgUrls:
        if "hotel-logo" in i:
            imgs.logo = i

    return render(
        request,
        "about.html",
        {
            "title": title,
            "name": name,
            "summary": summary,
            "address": address,
            "img": imgs,
        },
    )
