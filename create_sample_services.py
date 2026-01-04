from products.models import ServiceCategory, Service
import django
import os
cat > create_sample_services.py << 'EOF'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()


# Create categories
categories = [
    ('Web & Digital', 'Website design, development, and hosting', 'fa-globe'),
    ('Data Analytics', 'Business intelligence and data reporting', 'fa-chart-line'),
    ('Accounting Support', 'Financial data and bookkeeping support', 'fa-calculator'),
    ('Integrated Solutions', 'Combined accounting + analytics systems', 'fa-cogs'),
]

for name, desc, icon in categories:
    ServiceCategory.objects.get_or_create(
        name=name,
        defaults={'description': desc, 'icon': icon}
    )

# Create services
services = [
    # Web Services
    ('WordPress Website Development', 'Professional business website with custom design',
     'Web & Digital', 'one_time', 1999.99),
    ('E-commerce Setup', 'Online store with payment processing',
     'Web & Digital', 'one_time', 2999.99),
    ('Website Maintenance', 'Monthly updates, security, backups',
     'Web & Digital', 'subscription', 99.99),

    # Data Analytics
    ('Power BI Dashboard', 'Custom business performance dashboard',
     'Data Analytics', 'one_time', 1499.99),
    ('Data Cleanup Service', 'Prepare messy data for analysis',
     'Data Analytics', 'consultation', 75.00),
    ('Monthly Reporting', 'Regular performance reports',
     'Data Analytics', 'subscription', 199.99),

    # Accounting Support
    ('Bookkeeping Setup', 'System setup and process documentation',
     'Accounting Support', 'one_time', 899.99),
    ('Financial Data Audit', 'Review and cleanup of financial data',
     'Accounting Support', 'consultation', 85.00),

    # Integrated Solutions
    ('Business Intelligence System', 'Complete data + accounting reporting',
     'Integrated Solutions', 'one_time', 3999.99),
    ('Monthly CFO Insights', 'Regular financial + operational analysis',
     'Integrated Solutions', 'subscription', 299.99),
]

for name, desc, cat_name, service_type, price in services:
    category = ServiceCategory.objects.get(name=cat_name)
    Service.objects.get_or_create(
        name=name,
        defaults={
            'description': desc,
            'category': category,
            'service_type': service_type,
            'is_featured': True,
            'includes': 'Initial consultation, delivery, 30-day support',
            'deliverables': 'Complete project files, documentation, training',
        }
    )

print("Sample services created!")
