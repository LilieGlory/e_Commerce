from turtle import back
from django.urls import include, path

from product.views.productView import ProductList, ProductDetail, CreateNewProduct
from product.views.categoryView import CategoryDetail

urlpatterns = [
    path('product-list/', ProductList.as_view(), name='create'),
    path('category/<slug:category_name>/', CategoryDetail.as_view()),
    path('product-detail/<slug:category_name>/<slug:product_name>/', ProductDetail.as_view()),
    #path('product-create/', CreateNewProduct.index, name= 'index'),
]