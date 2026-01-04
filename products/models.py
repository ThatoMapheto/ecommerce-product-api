from django.db import models

class ServiceCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.name

class Service(models.Model):
    SERVICE_TYPES = [
        ('web', 'Web & Digital'),
        ('data', 'Data Analytics'),
        ('accounting', 'Accounting Support'),
        ('integrated', 'Integrated Solutions'),
    ]
    
    name = models.CharField(max_length=200)
    description = models.TextField()
    service_type = models.CharField(max_length=20, choices=SERVICE_TYPES)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    estimated_hours = models.PositiveIntegerField(null=True, blank=True)
    is_featured = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-is_featured', 'name']
    
    def __str__(self):
        return f"{self.name} (${self.price})"
    
    @property
    def display_type(self):
        return dict(self.SERVICE_TYPES)[self.service_type]
