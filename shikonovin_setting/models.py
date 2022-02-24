import os
from django.db import models


# Create your models here.
def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f'{instance.id}-{instance.title}{ext}'
    return f'logo/{final_name}'


# Create your models here.
class SiteSetting(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان سایت')
    address = models.CharField(max_length=500, verbose_name='آدرس')
    tell = models.CharField(max_length=50, verbose_name='تلفن تماس')
    fax = models.CharField(max_length=50, verbose_name='فکس')
    email = models.EmailField(max_length=150, verbose_name='میل')
    about_us = models.TextField(null=True, blank=True, verbose_name='درباره ی ما')
    copy_right = models.CharField(max_length=400, null=True, blank=True, verbose_name='متن کپی رایت')
    logo_site = models.ImageField(upload_to=upload_image_path, null=True, blank=True, verbose_name='لوگوی سایت')

    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural= 'مدیریت تنظیمات'

    def __str__(self):
        return self.title