from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MarketplacesViewSet

router = DefaultRouter()
router.register(r'', MarketplacesViewSet, basename='marketplaces')

urlpatterns = [
    path('', include(router.urls)),
]
