from rest_framework import serializers
from .models import Product

#cria ao link API
class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = '__all__' 