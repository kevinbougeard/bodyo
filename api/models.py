from django.db import models
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = PhoneNumberField()
    email = models.EmailField()


class Address(models.Model):
    type_of_address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = CountryField(blank=True)
    address_line = models.CharField(max_length=50)
    customer = models.ForeignKey(to=Customer, related_name='addresses', on_delete=models.CASCADE)
