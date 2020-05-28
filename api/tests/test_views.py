from django.test import Client
from rest_framework import status

from api.models import Customer
from api.serializers import CustomerSerializer
from api.tests import SetUpData

client = Client()


class CustomerViewTest(SetUpData):
    """ Test module for Customer views """

    def test_customers_list(self):
        response = client.get('/customer/')
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CityViewTest(SetUpData):
    """ Test module for City views """

    def test_find_customers_by_city(self):
        response = client.get('/city/Paris/')
        customer = Customer.objects.get(id=1)
        serializer = CustomerSerializer(customer)
        self.assertEqual(response.data, [serializer.data])
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class PhoneViewTest(SetUpData):
    """ Test module for Phone views """

    def test_find_customers_by_phone(self):
        response = client.get('/phone/+33102/')
        customer = Customer.objects.get(id=1)
        serializer = CustomerSerializer(customer)
        self.assertEqual(response.data, [serializer.data])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
