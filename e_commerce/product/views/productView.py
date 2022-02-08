import product
from product.models.product import Product
from product.serializer.productSerializer import ProductSerializer
from django.db.models import Q
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.renderers import TemplateHTMLRenderer


class ProductList(APIView):
    # renderer_classes = [TemplateHTMLRenderer]
    # template_name = 'product/product-list.html'

    def get(self, request, format = None):
        category_s_product = Product.objects.all()[0:10]
        serializer = ProductSerializer(category_s_product, many = True)
        # return Response(serializer.data)
        return Response({'products': serializer.data})

class ProductDetail(APIView):
    # renderer_classes = [TemplateHTMLRenderer]
    # template_name = 'product/product-detail.html'

    def get_object(self, product_name, category_name):
        try:
            return Product.objects.filter(Q(category__category_name = category_name) & Q(product_name__contains= product_name)).get()
        except Product.DoesNotExist:
            return Http404

    def get(self, request, product_name, category_name, format= None):
        product_research = self.get_object(product_name, category_name)
        serializer = ProductSerializer(product_research)
        return Response(serializer.data)
        # return Response({'product' : serializer.data})
