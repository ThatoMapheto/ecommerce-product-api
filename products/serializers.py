from rest_framework import serializers
from .models import ServiceCategory, Service

class ServiceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCategory
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    display_type = serializers.CharField(source='get_service_type_display', read_only=True)
    
    class Meta:
        model = Service
        fields = ['id', 'name', 'description', 'service_type', 'display_type', 
                 'price', 'estimated_hours', 'is_featured', 'is_available', 
                 'created_at']
        read_only_fields = ['created_at']
