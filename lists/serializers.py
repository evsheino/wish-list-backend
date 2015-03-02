from django.forms import widgets
from django.contrib.auth.models import User
from rest_framework import serializers
from lists.models import Category, Gift, Purchase

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase

class GiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gift

class GiftWithPurchasesSerializer(serializers.ModelSerializer):
    purchases = PurchaseSerializer(many=True)

    class Meta:
        model = Gift
        fields = ('url', 'created', 'modified', 'name', 'author', 'comment',
                'link', 'user', 'category', 'purchases',)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'first_name', 'last_name')
