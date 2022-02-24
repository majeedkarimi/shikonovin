from django.contrib import admin
from shikonovin_contact.models import ContactUs

# Register your models here.
class ContactUsAdmin(admin.ModelAdmin):
    list_display = [
        '__str__',
        'full_name',
        'email',
        'is_read'
    ]
    list_filter = ['is_read']
    list_editable = ['is_read','full_name']
    search_fields = ['subject', 'text']

admin.site.register(ContactUs, ContactUsAdmin)