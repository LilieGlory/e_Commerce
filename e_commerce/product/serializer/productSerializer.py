from rest_framework import serializers
from ..models.product import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "slug",
            "description",
            "price",
            "get_image",
            "get_thumbnail"
        )
