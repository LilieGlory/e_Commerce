# Generated by Django 4.0.1 on 2022-03-19 11:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(db_index=True, error_messages={'unique': 'this category is already taken'}, max_length=50, unique=True, validators=[django.core.validators.RegexValidator('^[a-zA-Z0-9_]+$', 'Enter a correct letters or number or _')]),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_number',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
