from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import ServiceCategory, Service, ServiceRequest
from .serializers import ServiceCategorySerializer, ServiceSerializer, ServiceRequestSerializer

class ServiceCategoryViewSet(viewsets.ModelViewSet):
    queryset = ServiceCategory.objects.all()
    serializer_class = ServiceCategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAdminUser()]
        return super().get_permissions()

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.filter(is_available=True)
    serializer_class = ServiceSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'service_type', 'is_featured']
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'base_price', 'created_at']
    ordering = ['-is_featured', 'name']
    
    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]

class ServiceRequestViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceRequestSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        if self.request.user.is_staff:
            return ServiceRequest.objects.all()
        return ServiceRequest.objects.filter(client=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(client=self.request.user)
