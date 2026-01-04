from rest_framework import serializers
from .models import ServiceCategory, Service, ServiceRequest

class ServiceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCategory
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    category = ServiceCategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=ServiceCategory.objects.all(),
        source='category',
        write_only=True
    )
    
    class Meta:
        model = Service
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

class ServiceRequestSerializer(serializers.ModelSerializer):
    service = ServiceSerializer(read_only=True)
    service_id = serializers.PrimaryKeyRelatedField(
        queryset=Service.objects.filter(is_available=True),
        source='service',
        write_only=True
    )
    
    class Meta:
        model = ServiceRequest
        fields = '__all__'
        read_only_fields = ('client', 'status', 'created_at', 'updated_at')
