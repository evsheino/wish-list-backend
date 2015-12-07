from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework.exceptions import NotAuthenticated
from lists.serializers import CategorySerializer, PurchaseSerializer, GiftSerializer, GiftWithPurchasesSerializer, UserSerializer
from lists.models import Category, Gift, Purchase
from lists.permissions import IsOwnerOrReadOnly, IsAuthenticatedNonOwner


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @detail_route()
    def purchases(self, request, pk, *args, **kwargs):
        """
        List the user's purchases.
        """

        if not request.user.is_authenticated():
            raise NotAuthenticated()

        return Response(PurchaseSerializer(self.get_object().purchases.
            exclude(gift__user=request.user), many=True).data)


class GiftViewSet(viewsets.ModelViewSet):
    queryset = Gift.objects.all()
    serializer_class = GiftSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    def list_user_gifts(self, request, user_pk, *args, **kwargs):
        """
        List the user's gift wishes.
        List purchases as well for authenticated non-owner users.
        """

        obj = User.objects.get(pk=user_pk)
        serializer_class = GiftWithPurchasesSerializer if request.user.is_authenticated() else GiftSerializer

        return Response(serializer_class(obj.gifts, many=True, context={'request': request}).data)


class PurchaseViewSet(viewsets.ModelViewSet):
    serializer_class = PurchaseSerializer
    permission_classes = (permissions.IsAuthenticated, IsAuthenticatedNonOwner,)

    def get_queryset(self):
        # Exclude purchases that are for gifts of the current user.
        return Purchase.objects.exclude(gift__user=self.request.user)
