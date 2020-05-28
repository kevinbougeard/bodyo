from api.models import Address, Customer
from api.tests import SetUpData


class CustomerTest(SetUpData):
    """ Test module for Customer model """

    def test_verbose_fields(self):
        customer = Customer.objects.get(id=1)
        first_name = customer._meta.get_field('first_name').verbose_name
        last_name = customer._meta.get_field('last_name').verbose_name
        self.assertEquals(first_name, 'first name')
        self.assertEquals(last_name, 'last name')

    def test_first_name_max_length(self):
        customer = Customer.objects.get(id=1)
        max_length = customer._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 50)


class AddressTest(SetUpData):
    """ Test module for Address model """

    def test_verbose_fields(self):
        address = Address.objects.get(id=1)
        type_of_address = address._meta.get_field('type_of_address').verbose_name
        city = address._meta.get_field('city').verbose_name
        self.assertEquals(type_of_address, 'type of address')
        self.assertEquals(city, 'city')

    def test_first_name_max_length(self):
        address = Address.objects.get(id=1)
        max_length = address._meta.get_field('type_of_address').max_length
        self.assertEquals(max_length, 50)
