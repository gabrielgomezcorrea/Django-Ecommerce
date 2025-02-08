from django.shortcuts import get_object_or_404, render

from apps.products.models import Category, Product


# Create your views here.


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(is_available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    return render(
        request,
        "products/product/list.html",
        {"category": category, "categories": categories, "products": products},
    )


def product_details(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, is_available=True)
    return render(request, "products/product/details.html", {"product": product})
