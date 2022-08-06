from rest_framework import viewsets
from products.models import *
from products.serializers import *


class ProductViewset(viewsets.ModelViewSet):
    model = Products
    queryset = Products.objects.all()
    serializer_class = ProductSerialziers

class OtherProductViewset(viewsets.ModelViewSet):
    model = OtherProducts
    queryset = OtherProducts.objects.all()
    serializer_class = OtherProductSerializers
