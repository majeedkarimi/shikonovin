import itertools
from django.shortcuts import render
from shikonovin_products.models import Product
from shikonovin_slider.models import Slider
from shikonovin_setting.models import SiteSetting


def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))



# code bihind home page
def home_page(request):
    most_visit_view = Product.objects.order_by('-visit_count').all()[:8]
    latest_products = Product.objects.order_by('-id').all()[:8]

    sildes = Slider.objects.all()
    context = {
        'slides': sildes,
        'most_visit_view':my_grouper(4,most_visit_view),
        'latest_products':my_grouper(4,latest_products),
    }
    return render(request, "home_page.html", context)


# code bihind header
def header(request, *args, **kwargs):
    setting = SiteSetting.objects.all().first()
    context= {
        'setting':setting,
    }
    return render(request, 'shared/Header.html', context)


# code bihind footer
def footer(request,*args,**kwargs):
    site_setiing=SiteSetting.objects.first()
    context= {
        'data':'کلیه حقوق مادی و معنوی این سایت برای شرکت شیک و نوین محفوظ می باشد',
        'sitesetting':site_setiing,
    }
    return render(request, 'shared/Footer.html', context)


def about_us(request):
    setting = SiteSetting.objects.all().first()
    context={
        'setting':setting,
    }
    return render(request, 'about_us.html', context)

