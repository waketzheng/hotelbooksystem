from django.db import models


ORDER_STATE_CHOICES = (
    ("will", "预定中"),
    ("run", "执行中"),
    ("end", "已结束"),
    ("destroyed", "已废弃"),
)


class Hotel(models.Model):
    tel = models.CharField("电话", max_length=30, null=True, blank=True)
    code = models.CharField("邮编", max_length=30, null=True, blank=True)
    name = models.CharField("名称", max_length=30, null=True, blank=True)
    address = models.CharField("地址", max_length=50, null=True)
    summary = models.TextField("简介", blank=True)
    logo = models.ImageField(upload_to="images", null=True, blank=True)
    order_background = models.ImageField(null=True, blank=True)
    overview = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Poster(models.Model):
    hotel = models.ForeignKey(Hotel, verbose_name="酒店", on_delete=None)
    img = models.ImageField("海报", upload_to="images", null=True)

    def __str__(self):
        return f"{self.hotle} {self.img.name}"


class Customer(models.Model):
    phone = models.CharField("手机", max_length=30)
    name = models.CharField("姓名", max_length=30, null=True, blank=True)
    id_card = models.CharField("身份证", max_length=30, null=True, blank=True)

    def __str__(self):
        return self.name


class RoomType(models.Model):
    hotel = models.ForeignKey(Hotel, verbose_name="酒店", on_delete=None)
    detail = models.CharField("类型", max_length=30, null=True, blank=True)
    price = models.IntegerField("价格", null=True, blank=True)
    image = models.ImageField(
        "image", upload_to="roomtype", null=True, blank=True
    )
    summary = models.TextField("简介", null=True, blank=True)

    def __str__(self):
        return self.detail


class Room(models.Model):
    name = models.CharField("房间号", max_length=30, primary_key=True)
    roomtype = models.ForeignKey(
        RoomType, verbose_name="房间类型", on_delete=None, null=True, blank=True
    )
    area = models.IntegerField("面积", null=True, blank=True)
    summary = models.TextField("简介", null=True, blank=True)

    @property
    def price(self):
        return getattr(self.roomtype, "price", 0)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, verbose_name="顾客", null=True
    )
    roomtype = models.ForeignKey(
        RoomType, verbose_name="房间类型", on_delete=None, null=True, blank=True
    )
    room = models.ForeignKey(Room, verbose_name="酒店", on_delete=None)
    begin = models.DateField("入住时间")
    end = models.DateField("离店时间")
    totalprice = models.IntegerField("需支付金额")
    state = models.CharField(
        "订单状态", max_length=45, choices=ORDER_STATE_CHOICES
    )

    def __str__(self):
        return self.id
