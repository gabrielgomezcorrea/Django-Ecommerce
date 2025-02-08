from django.contrib import admin

from apps.products.models import Category, Product

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "category",
        "name",
        "price",
        "is_available",
        "created_at",
        "updated_at",
    ]
    prepopulated_fields = {"slug": ("name",)}
