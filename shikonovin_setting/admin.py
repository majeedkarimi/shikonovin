from django.contrib import admin
from shikonovin_setting.models import SiteSetting

# Register your models here.
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = [
        '__str__',
        'tell',
    ]
admin.site.register(SiteSetting, SiteSettingAdmin)