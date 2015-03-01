from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from lists.serializers import CategorySerializer, PurchaseSerializer, GiftSerializer, GiftWithPurchasesSerializer, UserSerializer
from lists.models import Category, Gift, Purchase

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @detail_route()
    def purchases(self, request, pk, *args, **kwargs):
        return Response(GiftWithPurchasesSerializer(self.get_object().gifts, many=True).data)
