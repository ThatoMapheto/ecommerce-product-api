cat > README.md << 'EOF'
# E-commerce Product API

A complete Django REST Framework API for an online store with user authentication, product management, shopping cart, and order processing.

## 🚀 Features

### ✅ User Management
- Custom User model with email authentication
- JWT token-based authentication
- User profiles with additional information
- Password change functionality

### ✅ Product Management
- Product categories and organization
- Product CRUD operations (admin only)
- Product search and filtering
- Product reviews and ratings

### ✅ Shopping Cart
- Add/remove items from cart
- Update quantities
- Cart persistence per user
- Automatic total calculation

### ✅ Order System
- Convert cart to order
- Order status tracking (pending → processing → shipped → delivered → cancelled)
- Order history for users
- Admin order management
- Price preservation at time of purchase

### ✅ Admin Interface
- Full Django admin interface
- Manage users, products, categories, orders
- Order statistics and reports

## 🛠️ Tech Stack

- **Backend**: Django 6.0 + Django REST Framework
- **Authentication**: JWT with SimpleJWT
- **Database**: SQLite (development) / PostgreSQL (production ready)
- **File Storage**: Local (development) / AWS S3 ready (production)
- **API Documentation**: Ready for Swagger/OpenAPI integration

## 📦 Installation

```bash
# 1. Clone repository
git clone https://github.com/ThatoMapheto/ecommerce-product-api.git
cd ecommerce-product-api

# 2. Create virtual environment
python -m venv venv

# 3. Activate (Git Bash on Windows)
source venv/Scripts/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Configure environment (copy .env.example to .env)
cp .env.example .env
# Edit .env with your settings

# 6. Run migrations
python manage.py migrate

# 7. Create superuser
python manage.py createsuperuser

# 8. Run development server
python manage.py runserver