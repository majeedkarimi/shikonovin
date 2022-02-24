from django.shortcuts import render
from shikonovin_contact.forms import CreateContactForm
from shikonovin_contact.models import ContactUs
from shikonovin_setting.models import SiteSetting
# Create your views here.


def contact_page(request):
    contact_form = CreateContactForm(request.POST or None)
    if contact_form.is_valid():
        fullname = contact_form.cleaned_data.get('full_name')
        email = contact_form.cleaned_data.get('email')
        subject = contact_form.cleaned_data.get('subject')
        text = contact_form.cleaned_data.get('text')
        ContactUs.objects.create(full_name=fullname, email=email, subject=subject, text=text)
        # todo show user success message
        contact_form = CreateContactForm()
    site_setting=SiteSetting.objects.first()
    context={
        'contact_form':contact_form,
        'sitesetting':site_setting,
    }
    return render(request, 'contact_us/contact_us.html', context)

