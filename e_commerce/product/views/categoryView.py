import product
from product.models.category import Category
from product.models.product import Product
from product.serializer.categorySerializer import CategorySerializer

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.renderers import TemplateHTMLRenderer
from product.forms.categoryForm import CategoryForm


class CategoryDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'product/category.html'

    def get_object(self, category_name):
        try:
            category_research = Category.objects.get(category_name__contains= category_name)
            return category_research
        except Product.DoesNotExist:
            return Http404

    def get(self, request, category_name, format = None):
        category_research = self.get_object(category_name)
        serializer = CategorySerializer(category_research)
        return Response({'category': serializer.data})
        # return Response(serializer.data)