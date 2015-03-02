from django.forms import widgets
from django.contrib.auth.models import User
from rest_framework import serializers
from lists.models import Category, Gift, Purchase

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category

class PurchaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Purchase

class GiftSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gift

class GiftWithPurchasesSerializer(serializers.HyperlinkedModelSerializer):
    purchases = PurchaseSerializer(many=True)

    class Meta:
        model = Gift

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'first_name', 'last_name')
