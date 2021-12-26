from django.shortcuts import render

from shop.models import Category, Product, Image


def all_categories(request):
    return render(
        request,
        'all_categories.html',
        {
            'categories': Category.objects.all()
        },
    )


def all_products(request, pk):
    return render(
        request,
        'all_products.html',
        {
            'category': Category.objects.get(id=pk),
            'products': Product.objects.filter(category_id=pk)
        },
    )


def about_product(request, pk):
    return render(
        request,
        'about_product.html',
        {
            'product': Product.objects.get(id=pk),
            'images': Image.objects.filter(product_id=pk),
        },
    )
