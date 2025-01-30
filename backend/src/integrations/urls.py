from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IntegrationsViewSet

router = DefaultRouter()
router.register(r'', IntegrationsViewSet, basename='Integrations')

urlpatterns = [
    path('', include(router.urls)),
]
