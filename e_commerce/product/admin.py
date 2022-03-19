from django.contrib import admin


# Register your models here.
from product.models.category import Category
from product.models.product import Product
from product.models.cart import Cart


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)