from rest_framework import serializers
from .models import Product

class ProductSerializers(serializers.ModelSerializer):

    sale_price = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'sale_price']

    def get_sale_price(self, obj):
        return float(obj.price) * 0.8