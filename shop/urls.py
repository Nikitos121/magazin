from django.urls import path

from shop import views

urlpatterns = [
    path('categories/', views.all_categories),
    path('categories/<int:pk>/', views.all_products),
    path('products/<int:pk>/', views.about_product),

    # API
    path('api/categories/', views.CategoryListCreateAPIView.as_view()),
    path('api/categories/<int:pk>/', views.CategoryRetrieveUpdateDestroyAPIView.as_view()),
    path('api/products/', views.ProductListCreateAPIView.as_view()),
    path('api/products/<int:pk>/', views.ProductRetrieveUpdateDestroyAPIView.as_view()),
    path('api/products/<int:pk>/images/', views.ImageListCreateAPIView.as_view()),
    path('api/products/<int:product_id>/images/<int:pk>/', views.ImageRetrieveUpdateDestroyAPIView.as_view()),
]
