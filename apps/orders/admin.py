from django.contrib import admin
from apps.orders.models import Order, OrderItem

# Register your models here.


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ["product"]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "full_name", "email", "address", "is_paid", "created_at"]
    list_filter = ["is_paid", "created_at"]
    inlines = [OrderItemInline]
