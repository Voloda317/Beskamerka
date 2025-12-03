from django.contrib import admin

from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ("product_type", "product_name", "quantity", "price", "total_price_display")

    def total_price_display(self, obj):
        return obj.total_price
    total_price_display.short_description = "Сумма"


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "created_at", "user", "phone", "status", "total_price_display")
    list_filter = ("status", "created_at")
    search_fields = ("id", "user__username", "phone")
    inlines = [OrderItemInline]

    def total_price_display(self, obj):
        return obj.total_price
    total_price_display.short_description = "Сумма заказа"


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("id", "order", "product_name", "product_type", "quantity", "price")
    list_filter = ("product_type",)
    search_fields = ("product_name", "order__id")
