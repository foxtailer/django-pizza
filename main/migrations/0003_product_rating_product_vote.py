# Generated by Django 4.2 on 2024-11-08 15:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_product_ingredients'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rating',
            field=models.FloatField(default=0, validators=[django.core.validators.MaxValueValidator(5.0)]),
        ),
        migrations.AddField(
            model_name='product',
            name='vote',
            field=models.IntegerField(default=0),
        ),
    ]
