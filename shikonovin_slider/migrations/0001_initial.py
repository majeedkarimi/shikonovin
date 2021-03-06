# Generated by Django 3.2.4 on 2021-06-17 14:12

from django.db import migrations, models
import shikonovin_slider.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='عنوان')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('link', models.URLField(max_length=150, verbose_name='آدرس اینترنتی')),
                ('image', models.ImageField(blank=True, null=True, upload_to=shikonovin_slider.models.upload_image_path, verbose_name='تصیویر')),
            ],
            options={
                'verbose_name': 'اسلایدر',
                'verbose_name_plural': 'اسلایدرها',
            },
        ),
    ]
