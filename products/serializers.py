from .models import Product,Category,Order,OrderItem
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from users.serializers import CustomUserSerializer

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

class ProductSerializer(ModelSerializer):
    rating = serializers.StringRelatedField(many=True)
    category = CategorySerializer(read_only=True)
    class Meta:
        model = Product
        fields = ['name']

class OrderSerializer(ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    class Meta:
        model = Order
        fields = ['id', 'user', 'is_ordered', 'ordered_at']

class OrderItemSerializer(ModelSerializer):
    product = ProductSerializer()
    order = OrderSerializer()
    class Meta:
        model = OrderItem
        fields = ('id', 'product', 'order', 'quantity', 'get_total_product_price')