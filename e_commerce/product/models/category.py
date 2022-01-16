from django.db import models

# Category model
class Category(models.Model):
    name = models.CharField(max_length= 50, unique= True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_category_url(self):
        return f'/{self.name}/'
