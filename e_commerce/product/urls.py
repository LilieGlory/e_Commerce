from django.urls import include, path

from product.views.productView import ProductList, ProductDetail
from product.views.categoryView import CategoryDetail, CategoryForm

urlpatterns = [
    path('product-list/', ProductList.as_view()),
    path('category/<slug:category_name>/', CategoryDetail.as_view()),
    path('product-detail/<slug:category_name>/<slug:product_name>/', ProductDetail.as_view()),
]