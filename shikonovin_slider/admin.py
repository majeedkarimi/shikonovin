from django.contrib import admin
from .models import Slider


class SliderAdmin(admin.ModelAdmin):
    list_display = [
        '__str__',
        'title',
        'link',
    ]

    class Meta:
        model=Slider


# Register your models here.
admin.site.register(Slider, SliderAdmin)