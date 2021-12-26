from django.shortcuts import render, get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from shop.models import Category, Product, Image
from shop.serializers import CategorySerializer, ProductSerializer, ImageSerializer


def all_categories(request):
    return render(
        request,
        'all_categories.html',
        {
            'categories': Category.objects.all(),
        },
    )


def all_products(request, pk):
    return render(
        request,
        'all_products.html',
        {
            'category': get_object_or_404(Category, pk=pk),
            'products': Product.objects.filter(category_id=pk),
        },
    )


def about_product(request, pk):
    return render(
        request,
        'about_product.html',
        {
            'product': get_object_or_404(Product, pk=pk),
            'images': Image.objects.filter(product_id=pk),
        },
    )


class CategoryListCreateAPIView(ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class ProductListCreateAPIView(ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ImageListCreateAPIView(ListCreateAPIView):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()


class ImageRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()
