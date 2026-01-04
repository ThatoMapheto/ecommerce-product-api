from rest_framework import generics, permissions
from .models import ServiceCategory, Service
from .serializers import ServiceCategorySerializer, ServiceSerializer

class ServiceCategoryList(generics.ListAPIView):
    queryset = ServiceCategory.objects.all()
    serializer_class = ServiceCategorySerializer
    permission_classes = [permissions.AllowAny]

class ServiceList(generics.ListAPIView):
    serializer_class = ServiceSerializer
    permission_classes = [permissions.AllowAny]
    
    def get_queryset(self):
        queryset = Service.objects.filter(is_available=True)
        
        # Filter by service type if provided
        service_type = self.request.query_params.get('type', None)
        if service_type:
            queryset = queryset.filter(service_type=service_type)
        
        # Filter featured if requested
        featured = self.request.query_params.get('featured', None)
        if featured and featured.lower() == 'true':
            queryset = queryset.filter(is_featured=True)
        
        return queryset
