from django.db import models


class Cart(models.Model):
    """Корзина, привязанная к сессии (и опционально к пользователю в будущем)."""
    session_key = models.CharField(max_length=40, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Корзина {self.session_key}"

    @property
    def total_price(self):
        return sum(item.total_price for item in self.items.all())


class CartItem(models.Model):
    PRODUCT_TYPES = [
        ("tire", "Шина"),
        ("disk", "Диск"),
        ("akb", "Аккумулятор"),
    ]

    cart = models.ForeignKey(
        Cart,
        related_name="items",
        on_delete=models.CASCADE
    )
    product_type = models.CharField(
        max_length=10,
        choices=PRODUCT_TYPES
    )
    product_id = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField(default=1)
    price = models.IntegerField("Цена за единицу")  # фиксируем цену на момент добавления

    def __str__(self):
        return f"{self.product_type} #{self.product_id} x {self.quantity}"

    @property
    def total_price(self):
        return self.price * self.quantity

    @property
    def product(self):
        """Возвращает сам объект товара (шина, диск или акб)."""
        from tires.models import Tire
        from disks.models import Disk
        from akb.models import Akb

        model_map = {
            "tire": Tire,
            "disk": Disk,
            "akb": Akb,
        }
        model = model_map.get(self.product_type)
        if not model:
            return None
        try:
            return model.objects.get(id=self.product_id)
        except model.DoesNotExist:
            return None
