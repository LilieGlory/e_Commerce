from django.db import models
from django.db.models.deletion import CASCADE

from .category import Category
from io import BytesIO
from PIL import Image # thumbnail (resize an image)
from django.core.files import File

# Products model
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete= models.CASCADE, related_name= "category_s_product")
    product_name = models.CharField(max_length= 50)
    slug = models.SlugField()
    description = models.TextField(blank= True, null= True)
    image = models.ImageField(upload_to= 'images/')
    thumbnail = models.ImageField(upload_to= 'images/', blank=True, null= True)
    price = models.DecimalField(max_digits= 12, decimal_places=2)
    date = models.DateField(auto_now_add= True) # date d'ajout
    product_number = models.IntegerField(default=1)

    class Meta:
        ordering= ['-date']

    def __str__(self):
        return self.product_name

    def get_image(self):
        return 'http://127.0.0.1:8000'+self.image.url

    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000'+self.thumbnail.url
        else:
            img = Image.open(self.image) # load a PIL image instance from the image
            img.thumbnail((200,200)) # resize image
            thumb = BytesIO() # create a BytesIO file-like object to store
            img.save(thumb, 'JPEG', quality=85)
            self.thumbnail = File(thumb, name=self.image.name)
            self.save()

            return 'http://127.0.0.1:8000'+self.thumbnail.url

    def get_product_url(self):
        # return f'/{self.category.category_name}/{self.product_name}/'
        url = f'/{self.category.category_name}/{self.product_name}/'
        return 'http://127.0.0.1:8000/api/product-detail'+url