# Generated by Django 3.2.4 on 2021-06-22 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shikonovin_order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='تاریخ پرداخت'),
        ),
    ]
