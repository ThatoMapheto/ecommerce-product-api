#!/bin/bash

echo "=== Starting E-commerce API Demo ==="
echo ""

# 1. Start server in background
echo "1. Starting Django server..."
python manage.py runserver > server.log 2>&1 &
SERVER_PID=$!
sleep 5  # Give server time to start

echo "Server started with PID: $SERVER_PID"
echo ""

# 2. Test server status
echo "2. Testing server status..."
if curl -s http://127.0.0.1:8000/ > /dev/null; then
    echo "✅ Server is running"
else
    echo "❌ Server failed to start"
    cat server.log
    kill $SERVER_PID
    exit 1
fi
echo ""

# 3. Login to get token
echo "3. User authentication..."
LOGIN_RESPONSE=$(curl -s -X POST http://127.0.0.1:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "thatomapheto6@gmail.com",
    "password": "ThatoM@8508"
  }')

if echo "$LOGIN_RESPONSE" | grep -q "access"; then
    ACCESS_TOKEN=$(echo "$LOGIN_RESPONSE" | python -c "import sys, json; print(json.load(sys.stdin)['access'])")
    echo "✅ Login successful"
    echo "Token obtained: ${ACCESS_TOKEN:0:20}..."
else
    echo "❌ Login failed"
    echo "Response: $LOGIN_RESPONSE"
    kill $SERVER_PID
    exit 1
fi
echo ""

# 4. Create category
echo "4. Creating product category..."
CATEGORY_RESPONSE=$(curl -s -X POST http://127.0.0.1:8000/api/products/categories/ \
  -H "Authorization: Bearer $ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Electronics",
    "description": "Electronic devices and accessories"
  }')

if echo "$CATEGORY_RESPONSE" | grep -q "id"; then
    echo "✅ Category created successfully"
else
    echo "⚠️  Category may already exist or error occurred"
fi
echo ""

# 5. Create product
echo "5. Creating product..."
PRODUCT_RESPONSE=$(curl -s -X POST http://127.0.0.1:8000/api/products/ \
  -H "Authorization: Bearer $ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Wireless Bluetooth Headphones",
    "description": "Noise cancelling headphones with 30-hour battery",
    "price": 129.99,
    "category_id": 1,
    "stock_quantity": 25
  }')

if echo "$PRODUCT_RESPONSE" | grep -q "id"; then
    echo "✅ Product created successfully"
else
    echo "❌ Product creation failed"
    echo "Response: $PRODUCT_RESPONSE"
fi
echo ""

# 6. List products (public endpoint)
echo "6. Testing public product listing..."
PRODUCTS_LIST=$(curl -s -X GET http://127.0.0.1:8000/api/products/ \
  -H "Content-Type: application/json")

if echo "$PRODUCTS_LIST" | grep -q "results\|id"; then
    echo "✅ Products listed successfully"
    COUNT=$(echo "$PRODUCTS_LIST" | python -c "import sys, json; data=json.load(sys.stdin); print(len(data.get('results', data)) if isinstance(data, dict) else len(data))" 2>/dev/null || echo "?")
    echo "   Found $COUNT product(s)"
else
    echo "❌ Product listing failed"
fi
echo ""

# 7. Add to cart
echo "7. Testing shopping cart..."
CART_RESPONSE=$(curl -s -X POST http://127.0.0.1:8000/api/cart/add/ \
  -H "Authorization: Bearer $ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "product_id": 1,
    "quantity": 2
  }')

if echo "$CART_RESPONSE" | grep -q "success\|id"; then
    echo "✅ Item added to cart"
else
    echo "⚠️  Cart endpoint may not be implemented"
    echo "Response: $CART_RESPONSE"
fi
echo ""

# 8. Show admin URL
echo "8. Admin Interface:"
echo "   URL: http://127.0.0.1:8000/admin/"
echo "   Login with your superuser credentials"
echo ""

# 9. Show API endpoints
echo "9. Available API Endpoints:"
python manage.py show_urls 2>/dev/null | grep "^/api" | head -10
echo ""

# 10. Cleanup
echo "=== Demo Complete ==="
echo "Server is running. Press Ctrl+C to stop."
echo ""
echo "To stop server: kill $SERVER_PID"
echo ""

# Keep server running
wait $SERVER_PID
