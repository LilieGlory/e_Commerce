from rest_framework import serializers
from ..models.product import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "name",
            "slug",
            "description",
            "price",
            "get_image",
            "get_thumbnail",
            "get_product_url"
        )
