from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework_extensions.mixins import NestedViewSetMixin

from .models import Address, Customer
from .serializers import AddressSerializer, CustomerSerializer


class CustomerViewSet(NestedViewSetMixin, ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class AddressViewSet(NestedViewSetMixin, ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class CityViewSet(ReadOnlyModelViewSet):
    serializer_class = AddressSerializer
    lookup_field = 'city'
    queryset = ''

    def retrieve(self, request, *args, **kwargs):
        city = self.kwargs['city']
        addresses = Address.objects.filter(city=city).all()
        addresses = self.serializer_class(addresses, many=True).data
        customers_ids = list(set([address['customer'] for address in addresses]))
        customers = [CustomerSerializer(Customer.objects.get(pk=customer_id)).data for customer_id in customers_ids]
        return Response(customers, status=status.HTTP_200_OK)


class PhoneViewSet(ReadOnlyModelViewSet):
    serializer_class = CustomerSerializer
    lookup_field = 'phone_number'
    queryset = ''

    def retrieve(self, request, *args, **kwargs):
        phone_number = self.kwargs['phone_number']
        customers = Customer.objects.filter(phone_number__istartswith=phone_number).all()
        customers = self.serializer_class(customers, many=True).data
        return Response(customers, status=status.HTTP_200_OK)
