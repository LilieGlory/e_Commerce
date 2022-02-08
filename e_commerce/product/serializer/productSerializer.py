from rest_framework import serializers
from ..models.product import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "product_name",
            "slug",
            "description",
            "price",
            "product_number",
            "get_image",
            "get_thumbnail",
            "get_product_url"
        )
