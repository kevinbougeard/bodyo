from django.test import TestCase

from api.models import Address, Customer


class SetUpData(TestCase):
    @classmethod
    def setUpTestData(cls):
        customer_doe = Customer.objects.create(first_name="John",
                                               last_name="Doe",
                                               phone_number="+33102030405",
                                               email="john.doe@john.doe")

        customer_smith = Customer.objects.create(first_name="John",
                                                 last_name="Smith",
                                                 phone_number="+33201030405",
                                                 email="john.smith@john.smith")

        Address.objects.create(type_of_address="Test",
                               city="Paris",
                               country="FR",
                               address_line="Test",
                               customer=customer_doe)

        Address.objects.create(type_of_address="Test",
                               city="Strasbourg",
                               country="FR",
                               address_line="Test",
                               customer=customer_smith)
