from django.db import models

from houses.models import Room, RoomType
from members.models import Customer


class StatusChoices(models.TextChoices):
    will = "will", "预定中"
    run = "run", "执行中"
    end = "end", "已结束"
    destroy = "destroyed", "已废弃"


class Order(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, verbose_name="顾客", null=True
    )
    roomtype = models.ForeignKey(
        RoomType, verbose_name="房间类型", on_delete=models.SET_NULL, null=True, blank=True
    )
    room = models.ForeignKey(
        Room, verbose_name="酒店", on_delete=models.SET_NULL, null=True, blank=True
    )
    begin = models.DateField("入住时间")
    end = models.DateField("离店时间")
    totalprice = models.IntegerField("需支付金额")
    state = models.CharField("订单状态", max_length=45, choices=StatusChoices.choices)

    class Meta:
        verbose_name = verbose_name_plural = '订单'

    def __str__(self):
        return self.id
