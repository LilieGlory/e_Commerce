import product
from product.models.category import Category
from product.models.product import Product
from product.serializer.categorySerializer import CategorySerializer, CategoryCreateSerializer

from django.http import Http404, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.renderers import TemplateHTMLRenderer
from product.forms.categoryForm import CategoryForm
from django.shortcuts import render
from django.template import loader

class CategoryDetail(APIView):
    # renderer_classes = [TemplateHTMLRenderer]
    # template_name = 'product/category.html'

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

    def post(self, request, category_name):
        new_category = CategoryCreateSerializer(data = request.data)
        if new_category.is_valid(raise_exception=True):
            category_saved = new_category.save()
            return Response({"Success": "{} category add with success ".format(category_saved.category_name)})
        return Response("success")


"""class CreateNewCategory():
    def index(request):
        if request.method == "POST":
            form = CategoryForm(request.POST)
            if form.is_valid():
                return HttpResponse("mety")
        else:
            form = CategoryForm()
        
        template = loader.get_template('product/category.html')
        context = {
            "form" : form
        }
        return HttpResponse(template.render(context,request))"""