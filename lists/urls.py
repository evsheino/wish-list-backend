from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from lists import views

router = DefaultRouter()
router.register('users', views.UserViewSet)
router.register('categories', views.CategoryViewSet)
router.register('gifts', views.GiftViewSet)
router.register('purchases', views.PurchaseViewSet, base_name='purchases')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^users/(?P<user_pk>[0-9]+)/gifts/(?P<pk>[0-9]+)/$', 
        views.GiftViewSet.as_view({
            'get': 'retrieve',
            'put': 'update',
            'delete': 'destroy'
        })),
    url(r'^users/(?P<user_pk>[0-9]+)/gifts/$', 
        views.GiftViewSet.as_view({
            'get': 'list_user_gifts',
            'post': 'create'
        }))
]
