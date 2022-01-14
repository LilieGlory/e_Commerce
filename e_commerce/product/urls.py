from django.urls import include, path

from product import views

urlpatterns = [
    path('ecommerce/', views.ProductLayoutList.as_view()),
    path('category-product/<slug:category_name>/', views.CategoryDetail.as_view()),
]