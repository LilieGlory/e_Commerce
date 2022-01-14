from rest_framework import serializers
from ..models.category import Category
from .productSerializer import ProductSerializer

class CategorySerializer(serializers.ModelSerializer):
    category_s_product = ProductSerializer(many = True)
    
    class Meta:
        model = Category
        fields = (
            "name",
            "category_s_product"
        )