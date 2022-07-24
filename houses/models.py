from django.db import models


class Hotel(models.Model):
    tel = models.CharField("电话", max_length=30, null=True, blank=True)
    code = models.CharField("邮编", max_length=30, null=True, blank=True)
    name = models.CharField("名称", max_length=30, null=True, blank=True)
    address = models.CharField("地址", max_length=50, null=True)
    summary = models.TextField("简介", blank=True)
    logo = models.ImageField(upload_to="images", null=True, blank=True)
    order_background = models.ImageField(null=True, blank=True)
    overview = models.ImageField(null=True, blank=True)

    class Meta:
        verbose_name = verbose_name_plural = '酒店'

    def __str__(self):
        return self.name


class Poster(models.Model):
    hotel = models.ForeignKey(
        Hotel, verbose_name="酒店", on_delete=models.SET_NULL, null=True, blank=True
    )
    img = models.ImageField("海报", upload_to="images", null=True)

    class Meta:
        verbose_name = verbose_name_plural = '轮播图'

    def __str__(self):
        return f"{self.hotle} {self.img.name}"


class RoomType(models.Model):
    hotel = models.ForeignKey(
        Hotel, verbose_name="酒店", on_delete=models.SET_NULL, null=True, blank=True
    )
    detail = models.CharField("类型", max_length=30, null=True, blank=True)
    price = models.IntegerField("价格", null=True, blank=True)
    image = models.ImageField("image", upload_to="roomtype", null=True, blank=True)
    summary = models.TextField("简介", null=True, blank=True)

    class Meta:
        verbose_name = verbose_name_plural = '房间类型'

    def __str__(self):
        return self.detail


class Room(models.Model):
    name = models.CharField("房间号", max_length=30, primary_key=True)
    roomtype = models.ForeignKey(
        RoomType, verbose_name="房间类型", on_delete=models.SET_NULL, null=True, blank=True
    )
    area = models.IntegerField("面积", null=True, blank=True)
    summary = models.TextField("简介", null=True, blank=True)

    class Meta:
        verbose_name = verbose_name_plural = '房间'

    @property
    def price(self):
        return getattr(self.roomtype, "price", 0)

    def __str__(self):
        return self.name
