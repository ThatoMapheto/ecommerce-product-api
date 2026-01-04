from django.urls import path
from .views import ServiceCategoryList, ServiceList

urlpatterns = [
    path('categories/', ServiceCategoryList.as_view(), name='service-categories'),
    path('services/', ServiceList.as_view(), name='services'),
]
