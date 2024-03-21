from rest_framework.serializers import ModelSerializer, CharField

from .models import Product, Order, OrderItem


class OrderItemSerializer(ModelSerializer):
    name = CharField(source="product.name", read_only=True)

    class Meta:
        model = OrderItem
        fields = ['product', 'name', 'quantity']


class OrderSerializer(ModelSerializer):
    products = OrderItemSerializer(many=True, allow_empty=False)

    class Meta:
        model = Order
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'