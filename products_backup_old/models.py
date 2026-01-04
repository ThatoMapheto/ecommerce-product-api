from django.db import models


class ServiceCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    icon = models.CharField(max_length=50, blank=True)

    class Meta:
        verbose_name_plural = "Service Categories"
        ordering = ['name']

    def __str__(self):
        return self.name


class Service(models.Model):
    SERVICE_TYPES = [
        ('one_time', 'One-time Service'),
        ('subscription', 'Monthly Subscription'),
        ('consultation', 'Consultation/Hourly'),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(
        ServiceCategory, on_delete=models.CASCADE, related_name='services')
    service_type = models.CharField(max_length=20, choices=SERVICE_TYPES)
    base_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    hourly_rate = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    subscription_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    estimated_hours = models.PositiveIntegerField(null=True, blank=True)
    is_available = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    includes = models.TextField(blank=True)
    deliverables = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-is_featured', 'name']

    def __str__(self):
        return self.name

    @property
    def display_price(self):
        if self.service_type == 'one_time' and self.base_price:
            return f"${self.base_price} one-time"
        elif self.service_type == 'subscription' and self.subscription_price:
            return f"${self.subscription_price}/month"
        elif self.service_type == 'consultation' and self.hourly_rate:
            return f"${self.hourly_rate}/hour"
        return "Contact for pricing"


class ServiceRequest(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('reviewing', 'Reviewing'),
        ('quoted', 'Quoted'),
        ('approved', 'Approved'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    # Use string reference to avoid circular import
    client = models.ForeignKey(
        'users.User', on_delete=models.CASCADE, related_name='service_requests')
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='draft')

    business_name = models.CharField(max_length=200, blank=True)
    business_description = models.TextField(blank=True)
    specific_needs = models.TextField(blank=True)
    timeline = models.CharField(max_length=100, blank=True)
    budget_range = models.CharField(max_length=100, blank=True)

    preferred_date = models.DateField(null=True, blank=True)
    preferred_time = models.CharField(max_length=50, blank=True)
    duration_hours = models.PositiveIntegerField(default=1)

    quoted_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    final_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Service request for {self.service.name}"
