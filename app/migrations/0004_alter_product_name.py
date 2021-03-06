# Generated by Django 3.2.9 on 2021-11-19 20:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message='Length has to be 4-10 characters long. First letter has to be a digit or a letterOnly characters accepted are digits,letters,spaces or hyphens', regex='[0-9A-Za-z]([ 0-9A-Za-z-]){3,9}')]),
        ),
    ]
