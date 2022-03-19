from django.db import models

from product.models.product import Product

class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name= "product_cart")
    check_number = models.IntegerField(default=1)
    state = models.BooleanField()
    firstname = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    email = models.EmailField(null= True)
    date_added = models.DateField(auto_now_add=True)
