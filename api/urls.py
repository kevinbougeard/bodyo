from django.urls import include, path
from rest_framework.routers import DefaultRouter
from api.views import AddressViewSet, CustomerViewSet, CityViewSet, PhoneViewSet

from rest_framework_extensions.routers import NestedRouterMixin


class NestedDefaultRouter(NestedRouterMixin, DefaultRouter):
    pass


router = NestedDefaultRouter()

city_router = router.register('city', CityViewSet, basename='city')
phone_router = router.register('phone', PhoneViewSet, basename='phone')

customer_router = router.register('customer', CustomerViewSet)
customer_router.register(
    'address', AddressViewSet,
    basename='customer-address',
    parents_query_lookups=['customer'])

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
