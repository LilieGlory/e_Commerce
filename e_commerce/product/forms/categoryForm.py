from django.forms import ModelForm
from product.models.category import Category
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.core.validators import slug_re

class CategoryForm(ModelForm):
    def clean_category_name(self):
        category = self.cleaned_data['category_name']
        if not slug_re.match(category):
            raise ValidationError(
                self.error_messages['not_slug']
            )
        return category

    class Meta:
        model = Category
        fields = ['category_name']
        labels = { 'category_name': _("enter the new category  name")}