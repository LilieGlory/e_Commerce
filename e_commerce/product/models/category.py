from django.db import models
from django.core.validators import RegexValidator
VALIDATE_CATEGORY_NAME = RegexValidator(r'^[a-zA-Z0-9_]+$', 'Enter a correct letters or number or _')

# Category model
class Category(models.Model):
    # category_name = models.CharField(max_length= 50, unique= True, db_index= True , validators= [RegexValidator(r'^[a-zA-Z0-9_]+$', 'Enter letters or number or underscore')])
    category_name = models.CharField(max_length= 50, unique= True, db_index= True , validators= [VALIDATE_CATEGORY_NAME] ,error_messages={"unique":"this category is already taken"})

    class Meta:
        ordering = ["category_name"]

    def __str__(self):
        return self.category_name

    def get_category_url(self):
        return f'/{self.category_name}/'
