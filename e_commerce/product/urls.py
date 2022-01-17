from django.urls import include, path

from product import views

urlpatterns = [
    path('product-list/', views.ProductList.as_view()),
    path('product-category/<slug:category_name>/', views.CategoryDetail.as_view()),
    path('product-detail/<slug:category_name>/<slug:product_name>/', views.ProductDetail.as_view()),
]