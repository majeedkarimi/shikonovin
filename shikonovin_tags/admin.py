from django.contrib import admin
from shikonovin_tags.models import Tag

# Register your models here.

class TagAdmin(admin.ModelAdmin):
    list_display = [
        '__str__',
        'title',
        'slug',
        'active',
    ]

admin.site.register(Tag, TagAdmin)