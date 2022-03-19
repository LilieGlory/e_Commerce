from rest_framework import serializers
from product.models.product import Product

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

class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "category",
            "product_name",
            "slug",
            "description",
            "image",
            "price",
            "product_number"
        )

        extra_kwargs = {"category" : 
                            {
                                "error_messages": {
                                "blank": "Select the category", 
                                "invalid": "Incorrect type",
                                }
                            },
                        "slug" : 
                        {
                            "error_messages" : {
                                "blank" : "give a few description",
                                "invalid": "Enter a letters or number or _",
                            }
                        },
                        "price":
                        {
                            "error_messages" : {
                                "blank" : "the price",
                                "required" : "the price",
                            }
                        }

        }

    def validate_product_number(self, value):
        if value < 1:
            raise serializers.ValidationError("Product number must more than 0")
        return value

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("The price will be positive")
        return value