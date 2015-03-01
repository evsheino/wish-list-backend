from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from lists import views

router = DefaultRouter()
router.register('users', views.UserViewSet)
router.register('categories', views.CategoryViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
