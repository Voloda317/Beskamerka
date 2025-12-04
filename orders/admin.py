from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    fields = (
        "product_name",
        "product_art",
        "product_type",
        "quantity",
        "price",
        "total_price_display",
    )
    readonly_fields = (
        "product_name",
        "product_art",
        "product_type",
        "quantity",
        "price",
        "total_price_display",
    )

    def total_price_display(self, obj):
        return obj.total_price
    total_price_display.short_description = "Сумма"


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "phone",
        "created_at",
        "status",
        "products_display",
        "total_price_display",
    )

    # Делаем столбец "статус" изменяемым прямо в списке
    list_editable = ("status",)

    list_filter = ("status", "created_at")
    search_fields = ("id", "user__username", "phone")
    readonly_fields = ("created_at", "updated_at", "total_price_display")
    inlines = [OrderItemInline]
    date_hierarchy = "created_at"
    ordering = ("-created_at",)

    def total_price_display(self, obj):
        return obj.total_price
    total_price_display.short_description = "Сумма заказа"

    def products_display(self, obj):
        """Показываем товары и артикулы в списке заказов."""
        items = obj.items.all()
        if not items:
            return "-"
        return ", ".join(
            f"{item.product_name} ({item.product_art or '-'})"
            for item in items
        )
    products_display.short_description = "Товары"


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "order",
        "product_name",
        "product_art",
        "product_type",
        "quantity",
        "price",
        "total_price",
    )
    list_filter = ("product_type",)
    search_fields = ("product_name", "product_art", "order__id")
