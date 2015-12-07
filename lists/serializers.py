from django.contrib.auth.models import User
from rest_framework import serializers
from lists.models import Category, Gift, Purchase


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class GiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gift
        fields = ('id', 'created', 'modified', 'name', 'author', 'comment',
                'link', 'user', 'category',)


class UserSerializer(serializers.ModelSerializer):
    gifts = GiftSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'gifts',)


class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = ('id', 'created', 'modified', 'comment', 'user', 'gift',)


class GiftWithPurchasesSerializer(serializers.ModelSerializer):
    purchases = PurchaseSerializer(many=True)

    class Meta:
        model = Gift
        fields = ('id', 'created', 'modified', 'name', 'author', 'comment',
                'link', 'user', 'category', 'purchases',)
