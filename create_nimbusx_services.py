from products.models import ServiceCategory, Service
import django
import sys
import os
cat > create_nimbusx_services.py << 'EOF'
#!/usr/bin/env python

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    django.setup()
except Exception as e:
    print(f"Error setting up Django: {e}")
    sys.exit(1)


print("=== Creating NimbusX Services ===")

# Create or get categories
categories_data = [
    ('Web & Digital Solutions',
     'WordPress websites, e-commerce, hosting, maintenance', 'fa-globe'),
    ('Data Analytics & BI',
     'Power BI dashboards, data cleanup, business reporting', 'fa-chart-line'),
    ('Accounting Support',
     'Bookkeeping setup, financial data audits, management accounts', 'fa-calculator'),
    ('Integrated Solutions',
     'Combined accounting + analytics systems, business intelligence', 'fa-cogs'),
]

categories = {}
for name, desc, icon in categories_data:
    cat, created = ServiceCategory.objects.get_or_create(
        name=name,
        defaults={'description': desc, 'icon': icon}
    )
    categories[name] = cat
    status = "Created" if created else "Exists"
    print(f"{status}: {name}")

print("\n=== Creating Services ===")

services_data = [
    # Web & Digital Solutions
    ('WordPress Website Development', 'Professional business website with custom design, responsive layout, and basic SEO',
     'Web & Digital Solutions', 'one_time', 1999.99, None, None, True),
    ('E-commerce Store Setup', 'Online store with payment processing, inventory management, and security',
     'Web & Digital Solutions', 'one_time', 2999.99, None, None, True),
    ('Website Maintenance Plan', 'Monthly updates, security monitoring, backups, and performance optimization',
     'Web & Digital Solutions', 'subscription', None, None, 99.99, True),
    ('Business Email & Hosting', 'Professional email setup with domain hosting and security',
     'Web & Digital Solutions', 'subscription', None, None, 29.99, False),

    # Data Analytics & BI
    ('Power BI Dashboard Creation', 'Custom business performance dashboard with real-time data',
     'Data Analytics & BI', 'one_time', 1499.99, None, None, True),
    ('Data Cleanup & Preparation', 'Transform messy spreadsheets into clean, analysis-ready data',
     'Data Analytics & BI', 'consultation', None, 75.00, None, True),
    ('Monthly Business Reports', 'Regular performance analysis with insights and recommendations',
     'Data Analytics & BI', 'subscription', None, None, 199.99, True),
    ('Data Audit & Quality Check', 'Comprehensive review of your data systems and quality',
     'Data Analytics & BI', 'consultation', None, 85.00, None, False),

    # Accounting Support
    ('Bookkeeping System Setup', 'Complete bookkeeping process setup with documentation',
     'Accounting Support', 'one_time', 899.99, None, None, True),
    ('Financial Data Cleanup', 'Review and cleanup of accounting data for accuracy',
     'Accounting Support', 'consultation', None, 85.00, None, True),
    ('Monthly Financial Review', 'Regular review of financial position and cash flow',
     'Accounting Support', 'subscription', None, None, 149.99, False),

    # Integrated Solutions
    ('Business Intelligence System', 'Complete integrated accounting + operations reporting',
     'Integrated Solutions', 'one_time', 3999.99, None, None, True),
    ('Monthly CFO Insights', 'Regular financial + operational analysis for decision-making',
     'Integrated Solutions', 'subscription', None, None, 299.99, True),
    ('Strategic Planning Session', '1-on-1 business strategy and growth planning',
     'Integrated Solutions', 'consultation', None, 120.00, None, True),
]

for name, desc, cat_name, service_type, base_price, hourly_rate, subscription_price, featured in services_data:
    service, created = Service.objects.get_or_create(
        name=name,
        defaults={
            'description': desc,
            'category': categories[cat_name],
            'service_type': service_type,
            'base_price': base_price,
            'hourly_rate': hourly_rate,
            'subscription_price': subscription_price,
            'estimated_hours': 10 if service_type == 'one_time' else None,
            'is_featured': featured,
            'includes': 'Initial consultation, detailed proposal, delivery, 30-day support',
            'deliverables': 'Complete project files, documentation, training session, support access',
        }
    )
    status = "Created" if created else "Exists"
    price_display = service.display_price
    print(f"{status}: {name} ({price_display})")

print(f"\n=== Summary ===")
print(f"Categories: {ServiceCategory.objects.count()}")
print(f"Services: {Service.objects.count()}")
print(f"Featured Services: {Service.objects.filter(is_featured=True).count()}")
print("\nNimbusX Services Platform is ready!")
EOF
