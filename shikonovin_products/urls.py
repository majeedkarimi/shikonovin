from django.urls import path
from .views import ProductsList, product_detail, SearchProductList, ProductsListByCategories, products_category_partial


urlpatterns = [
    path('products/', ProductsList.as_view()),
    path('product-detail/<productid>/<title>', product_detail),
    path('products/search', SearchProductList.as_view()),
    path('products/<category_name>', ProductsListByCategories.as_view()),
    path('products_category_partial', products_category_partial, name='product_category_partial' )
]