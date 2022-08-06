from rest_framework import serializers
from .models import *


class ProductSerialziers(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'


class OtherProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = OtherProducts
        fields = '__all__'