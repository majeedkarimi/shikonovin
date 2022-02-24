from django.urls import path
from shikonovin_order.views import add_user_order, cart_order_detail, send_request, verify, delete_order_detail

urlpatterns = [
    path('add-user-order',add_user_order),
    path('cart_order_detail', cart_order_detail),
    path('request/', send_request, name='request'),
    path('verify/<order_id>', verify, name='verify'),
    path('remove_order_detail/<detail_id>', delete_order_detail)

]
