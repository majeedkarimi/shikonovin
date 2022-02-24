from django.db import models
import os

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f'{instance.id}-{instance.title}{ext}'
    return f'slider/{final_name}'

# Create your models here.
class Slider(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    link = models.URLField(max_length=150, verbose_name='آدرس اینترنتی')
    image = models.ImageField(upload_to=upload_image_path, blank=True, null=True, verbose_name='تصیویر')

    class Meta:
        verbose_name='اسلایدر'
        verbose_name_plural='اسلایدرها'

    def __str__(self):
        return self.title