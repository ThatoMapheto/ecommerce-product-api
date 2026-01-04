from django.contrib import admin
from .models import ServiceCategory, Service

@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'service_type', 'price', 'is_featured', 'is_available')
    list_filter = ('service_type', 'is_featured', 'is_available')
    search_fields = ('name', 'description')
