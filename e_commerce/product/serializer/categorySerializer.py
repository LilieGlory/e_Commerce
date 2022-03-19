from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from ..models.category import Category
from .productSerializer import ProductSerializer
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

class CategorySerializer(serializers.ModelSerializer):
    category_s_product = ProductSerializer(many = True)
    
    class Meta:
        model = Category
        fields = (
            "category_name",
            "get_category_url",
            "category_s_product",
        )

class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        extra_kwargs = {"category_name" : 
                            {
                                "error_messages": {
                                "blank": "Give your new category", 
                                "invalid": "Enter letter or number or _",
                                }
                            }
                        }