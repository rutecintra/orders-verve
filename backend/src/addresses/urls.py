from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AddressesViewSet

router = DefaultRouter()
router.register(r'', AddressesViewSet, basename='addresses')

urlpatterns = [
    path('', include(router.urls)),
]