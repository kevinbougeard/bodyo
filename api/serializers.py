from abc import ABC

from rest_framework.serializers import ModelSerializer, RelatedField

from .models import Address, Customer


class AddressListingField(RelatedField, ABC):
    def to_representation(self, value):
        return AddressSerializer(value).data


class CustomerSerializer(ModelSerializer):
    addresses = AddressListingField(many=True, read_only=True)

    class Meta:
        model = Customer
        fields = ("id", "first_name", "last_name", "phone_number", "email", "addresses")


class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = ("id", "type_of_address", "city", "country", "address_line", "customer")
