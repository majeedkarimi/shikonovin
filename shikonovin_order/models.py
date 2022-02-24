from django.db import models
from django.contrib.auth.models import User
from shikonovin_products.models import Product

# Create your models here.


class Order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='نام کاربر')
    is_paid = models.BooleanField(verbose_name='پرداخت شده/ نشده')
    payment_date = models.DateTimeField(blank=True, null=True, verbose_name='تاریخ پرداخت')
    ref_id = models.IntegerField(null=True, blank=True, verbose_name='شماره پیگیری')

    def total_order_price(self):
        total = 0
        for detail in self.orderdetail_set.all():
            total += detail.count * detail.price
        return total

    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبدهای خرید کاربران'

    def __str__(self):
        return self.owner.get_full_name()


class OrderDetail(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='سبد خرید')
    price = models.IntegerField(verbose_name='قیمت محصول')
    count = models.IntegerField(verbose_name='تعداد محصول')

    def total_price(self):
        return self.price * self.count

    class Meta:
        verbose_name = 'جزِِئیات محصول'
        verbose_name_plural = 'اطلاعات جزئیات خرید'

    def __str__(self):
        return self.product.title

