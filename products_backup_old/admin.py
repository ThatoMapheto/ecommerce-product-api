from django.contrib import admin
from .models import ServiceCategory, Service, ServiceRequest

@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'icon')
    search_fields = ('name', 'description')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'service_type', 'display_price', 'is_available', 'is_featured')
    list_filter = ('category', 'service_type', 'is_available', 'is_featured')
    search_fields = ('name', 'description')
    readonly_fields = ('display_price',)

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('client', 'service', 'status', 'business_name', 'created_at')
    list_filter = ('status', 'service__category', 'created_at')
    search_fields = ('client__email', 'business_name', 'service__name')
    readonly_fields = ('created_at', 'updated_at')
