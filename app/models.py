from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone
from django.core.exceptions import ValidationError

def validate_date(date):
    if date < timezone.now().date():
        raise ValidationError('Start date cannot be earlier than current date')

class Product(models.Model):
    name = models.CharField(unique=True,
                            max_length=10,
                            validators=[RegexValidator(regex='^[0-9A-Za-z]([ 0-9A-Za-z-]){3,9}$',
                                                                     message='Length has to be 4-10 characters long. First letter has to be a digit or a letter '
                                                                             'Only characters accepted are digits,letters,spaces or hyphens')])
    price = models.IntegerField()
    start_date = models.DateField(validators=[validate_date])

