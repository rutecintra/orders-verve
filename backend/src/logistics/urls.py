from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LogisticsViewSet

router = DefaultRouter()
router.register(r'', LogisticsViewSet, basename='logistics')

urlpatterns = [
    path('', include(router.urls)),
]
