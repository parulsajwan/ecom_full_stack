
from rest_framework import serializers
from .models import Order
from products.models import Product
from django.contrib.auth.models import User


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    product = ProductDetailSerializer()
    user = UserDetailSerializer()

    class Meta:
        model = Order
        fields = ('id', 'user', 'product')
