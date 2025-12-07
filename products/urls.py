from django.urls import path
from .views import (
    CategoryListCreateView, CategoryDetailView,
    ProductListView, ProductDetailView, ProductSearchView,
    ReviewListView
)

urlpatterns = [
    # Categories
    path('categories/', CategoryListCreateView.as_view(), name='category-list'),
    path('categories/<int:id>/', CategoryDetailView.as_view(),
         name='category-detail'),

    # Products
    path('', ProductListView.as_view(), name='product-list'),
    path('<int:id>/', ProductDetailView.as_view(), name='product-detail'),
    path('search/', ProductSearchView.as_view(), name='product-search'),

    # Reviews
    path('<int:product_id>/reviews/',
         ReviewListView.as_view(), name='product-reviews'),
]
