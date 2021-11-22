# Generated by Django 3.2.9 on 2021-11-19 21:28

import app.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=10, unique=True, validators=[django.core.validators.RegexValidator(message='Length has to be 4-10 characters long. First letter has to be a digit or a letter Only characters accepted are digits,letters,spaces or hyphens', regex='^[0-9A-Za-z]([ 0-9A-Za-z-]){3,9}$')]),
        ),
        migrations.AlterField(
            model_name='product',
            name='start_date',
            field=models.DateField(validators=[app.models.validate_date]),
        ),
    ]