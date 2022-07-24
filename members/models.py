from django.db import models


class Customer(models.Model):
    phone = models.CharField("手机", max_length=30)
    name = models.CharField("姓名", max_length=30, null=True, blank=True)
    id_card = models.CharField("身份证", max_length=30, null=True, blank=True)

    class Meta:
        verbose_name = verbose_name_plural = '客户'

    def __str__(self):
        return self.name
