from django.shortcuts import render
from django.http import Http404

import product

# Create your views here.
from .models.category import Category
from .models.product import Product
from product.serializer.productSerializer import ProductSerializer
from .serializer.categorySerializer import CategorySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q

class ProductList(APIView):
    def get(self, request, format = None):
        category_s_product = Product.objects.all()[0:6]
        serializer = ProductSerializer(category_s_product, many = True)
        return Response(serializer.data)

class CategoryDetail(APIView):
    def get_object(self, category_name):
        try:
            category_research = Category.objects.get(name__contains= category_name)
            return category_research
        except Product.DoesNotExist:
            return Http404

    def get(self, request, category_name, format = None):
        category_research = self.get_object(category_name)
        serializer = CategorySerializer(category_research)
        return Response(serializer.data)

class ProductDetail(APIView):
    def get_object(self, product_name, category_name):
        try:
            return Product.objects.filter(Q(category__name = category_name) & Q(name__contains= product_name)).get()
        except Product.DoesNotExist:
            return Http404

    def get(self, request, product_name, category_name, format= None):
        product_research = self.get_object(product_name, category_name)
        serializer = ProductSerializer(product_research)
        return Response(serializer.data)
