from django.contrib import admin
from .models import Product, ProductGallery


# edite culomns admin
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        '__str__',
        'title',
        'price',
        'active'
    ]

    class Meta:
        Model=Product

class ProductGalleryAdmin(admin.ModelAdmin):
    list_display = [
        '__str__',
        'title',
    ]
    class Meta:
        model=ProductGallery


# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductGallery, ProductGalleryAdmin)

