from django.shortcuts import render
from django.http import Http404

# Create your views here.
from .models.category import Category
from .models.product import Product
from product.serializer.productSerializer import ProductSerializer
from .serializer.categorySerializer import CategorySerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class ProductLayoutList(APIView):
    def get(self, request, format = None):
        category_s_product = Product.objects.all()[0:6]
        serializer = ProductSerializer(category_s_product, many = True)
        return Response(serializer.data)

class CategoryDetail(APIView):
    def get_object(self, category_name):
        try:
            # category_research = Category.objects.get(name__contains= category_name)
            category_research = Category.objects.get(name__contains= category_name)
            return category_research
        except Product.DoesNotExist:
            return Http404

    def get(self, request, category_name, format = None):
        category = self.get_object(category_name)
        serializer = CategorySerializer(category)
        return Response(serializer.data)
