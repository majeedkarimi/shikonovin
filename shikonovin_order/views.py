import time

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from shikonovin_order.forms import UserNewOrderForm
from shikonovin_order.models import Order, OrderDetail
from shikonovin_products.models import Product
from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from zeep import Client


# Create your views here.

@login_required(login_url = '/login')
def add_user_order(request):
    # if not request.user.is_authenticated:
    #     return redirect('/login')
    # else:
    user_new_order_form = UserNewOrderForm(request.POST or None )

    if user_new_order_form.is_valid():
        order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
        if order is None:
            order = Order.objects.create(owner_id=request.user.id, is_paid=False)

        product_id = user_new_order_form.cleaned_data.get('product_id')
        count = user_new_order_form.cleaned_data.get('count')
        if count <=0:
            count = 1
        product = Product.objects.get_by_id(product_id=product_id)
        order.orderdetail_set.create(product_id=product_id, count=count, price=product.price)
        return redirect(f'/product-detail/{product.id}/{product.title.replace(" ","-")}')
    return redirect('/')


@login_required(login_url='/login')
def cart_order_detail(request):
    context ={
        'order': None,
        'details': None,
        'total_price': 0,
    }
    open_order: Order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
    if open_order is not None:
        context['order'] = open_order
        context['details'] = open_order.orderdetail_set.all()
        context['total_price'] = open_order.total_order_price()
    return render(request, 'cart_order_detail.html', context)



MERCHANT = 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'
amount = 1000  # Toman / Required
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
email = 'email@example.com'  # Optional
mobile = '09123456789'  # Optional
client = Client('https://www.zarinpal.com/pg/services/WebGate/wsdl')
CallbackURL = 'http://localhost:8000/verify/' # Important: need to edit for realy server.


def send_request(request):
    total_price = 0
    open_order: Order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
    if open_order is not None:
        total_price = open_order.total_order_price()
        result = client.service.PaymentRequest(MERCHANT, total_price, description, email, mobile, f'{CallbackURL}/{open_order.id}')
        if result.Status == 100:
            return redirect('https://www.zarinpal.com/pg/StartPay/' + str(result.Authority))
        else:
            return HttpResponse('Error code: ' + str(result.Status))
    raise Http404('سفارش کالایی انجام نشده است')


def verify(request, *args, **kwargs):
    order_id = kwargs['order_id']

    if request.GET.get('Status') == 'OK':
        result = client.service.PaymentVerification(MERCHANT, request.GET['Authority'], amount)
        if result.Status == 100:
            order = Order.objects.get_queryset().filter(order_id=order_id).first()
            order.is_paid = True
            order.payment_date = time.time()
            order.ref_id = result.RefID
            order.save()
            return HttpResponse('Transaction success.\nRefID: ' + str(result.RefID))
        elif result.Status == 101:
            return HttpResponse('Transaction submitted : ' + str(result.Status))
        else:
            return HttpResponse('Transaction failed.\nStatus: ' + str(result.Status))
    else:
        return HttpResponse('Transaction failed or canceled by user')


@login_required(login_url='/login')
def delete_order_detail(request, *args, **kwargs):
    order_detail = kwargs.get('detail_id')
    if order_detail is not None:
        order_detail = OrderDetail.objects.filter(id=order_detail, order__owner_id=request.user.id).first()
        if order_detail is not None:
            order_detail.delete()
        return redirect('/cart_order_detail')
    raise Http404()