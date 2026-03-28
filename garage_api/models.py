from decimal import Decimal

from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models

# Create your models here.

class TimeStampModelMixin(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Manufacturer(TimeStampModelMixin):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    founded_year = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class Car(TimeStampModelMixin):
    model = models.CharField(max_length=100, validators=[MinLengthValidator(2)])
    verified = models.BooleanField(default=False)
    year = models.PositiveIntegerField(validators=[MinValueValidator(1900)])
    price = models.DecimalField(max_digits=10, decimal_places=2,)
    manufacturer = models.ForeignKey(to=Manufacturer, related_name='cars', on_delete=models.CASCADE)


class Part(TimeStampModelMixin):
    name = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(limit_value=Decimal('0.01'), message="Price has to be a positive number")]
    )
    manufacturer = models.ForeignKey(to=Manufacturer, related_name='parts', on_delete=models.CASCADE)
    cars = models.ManyToManyField(to=Car, related_name='parts')