from django import forms
from django.core.validators import RegexValidator
from . import models


# class ProductForm(forms.Form):
#     name = forms.CharField(label="Name",
#                            required=True,
#                            max_length=10,
#                            validators=[RegexValidator(regex='^[0-9A-Za-z]([ 0-9A-Za-z-]){3,9}$',
#                                                       message='Length has to be 4-10 characters long. First letter has to be a digit or a letter '
#                                                               'Only characters accepted are digits,letters,spaces or hyphens')])
#     price = forms.IntegerField(label="Price",
#                                required=True)
#     start_date = forms.DateField(label="Post Date",
#                                  required=True,
#                                  validators=[models.validate_date])

class ProductForm(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = ['name','price','start_date']