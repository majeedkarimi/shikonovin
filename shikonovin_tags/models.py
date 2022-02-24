from django.db import models

from shikonovin_products.models import Product
from .utils import unique_slug_generator
from django.db.models.signals import pre_save, post_save


class Tag(models.Model):  # Create your models here.
    title=models.CharField(max_length=150, verbose_name='عنوان')
    slug=models.SlugField(verbose_name='عنوان در url')
    timestamp=models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')
    active=models.BooleanField(default=True, verbose_name='فعال / غیرفعال')
    product=models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural='برچسب ها'
        verbose_name='برچسب'


def tag_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(tag_pre_save_receiver, sender=Tag)





