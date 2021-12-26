from django.urls import path

from shop.views import all_categories, all_products, about_product

urlpatterns = [
    path('categories/', all_categories),
    path('categories/<int:pk>/', all_products),
    path('products/<int:pk>/', about_product),
]
