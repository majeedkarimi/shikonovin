import itertools

from django.shortcuts import render
from django.views.generic import ListView

from shikonovin_order.forms import UserNewOrderForm
from shikonovin_tags.models import Tag
from .models import Product, ProductGallery
from django.http import Http404
from shikonovin_products_category.models import ProductCategory


# Create your views here.
class ProductsList(ListView):
    template_name = 'products/products_list.html'
    paginate_by = 6

    def get_queryset(self):
        return Product.objects.get_active_products()

class ProductsListByCategories(ListView):
    template_name = 'products/products_list.html'
    paginate_by = 2

    def get_queryset(self):
        category_name=self.kwargs['category_name']
        category = ProductCategory.objects.filter(name__iexact=category_name).first()
        if not category:
            raise Http404('محصول مورد نظر یافت نشد')
        return Product.objects.get_product_by_category(category_name)


def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


def product_detail(request, *args, **kwargs):
    product_id = kwargs['productid']
    new_order_form=UserNewOrderForm(request.POST or None, initial={'product_id':product_id})
# Product.objects.filter(id=product_id)
    product = Product.objects.get_by_id(product_id)

    product.visit_count += 1
    product.save()

    if product is None or product.active is False:
        raise Http404('صفحه ی مورد نظر یافت نشد')
    galleries = ProductGallery.objects.filter(product_id=product_id)
    grouped_gallery = list(my_grouper(3, galleries))
    # print(grouped_gallery)

    recommended_products = Product.objects.get_queryset().filter(categories__product=product).distinct()
    list_recommended_products = list(my_grouper(3,recommended_products))
    context = {
        'product': product,
        'galleries': grouped_gallery,
        'recommended_products': list_recommended_products,
        'new_order_form':new_order_form,

    }




    # tag=Tag.objects.first()
    # print(tag.product.all())
    #
    # print(product.tag_set.all())

    return render(request, 'products/product_detail.html', context)


class SearchProductList(ListView):
    template_name = 'products/products_list.html'
    paginate_by = 6

    def get_queryset(self):
        request=self.request
        query = request.GET.get('query')
        if query is not None:
            return Product.objects.search(query)  # search in models>Product>ProductManager
        return Product.objects.get_active_products()


''' 
        /products/search/?query=majid&name=majid&family=karimi
        self.request >> <WSGIRequest: GET '/products/search?query=majid&name=majid&family=karimi'>
        self.request.GET >> <QueryDict: {'query': ['majid'], 'name': ['majid'], 'family': ['karimi']}>
        self.request.GET.get('query') >> majid
'''

'''
        
        __icontains => return fields contain this
        __iexact => return fields exactly this
        
'''

def products_category_partial(request):
    categories=ProductCategory.objects.all()

    context = {
        'categories':categories,
    }
    return  render(request, 'products/products_category.html', context)