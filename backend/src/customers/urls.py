from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomersViewSet

router = DefaultRouter()
router.register(r'', CustomersViewSet, basename='Customers')

urlpatterns = [
    path('', include(router.urls)),
]
