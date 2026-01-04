from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ServiceCategoryViewSet, ServiceViewSet, ServiceRequestViewSet

router = DefaultRouter()
router.register(r'categories', ServiceCategoryViewSet, basename='category')
router.register(r'services', ServiceViewSet, basename='service')
router.register(r'requests', ServiceRequestViewSet, basename='request')

urlpatterns = [
    path('', include(router.urls)),
]
