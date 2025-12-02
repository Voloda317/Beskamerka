from django.db import models


class Cart(models.Model):
    """
    Корзина, привязанная к сессии.
    В будущем сюда можно добавить ForeignKey на пользователя.
    """
    session_key = models.CharField(max_length=40, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"

    def __str__(self):
        return f"Корзина #{self.pk}"


class CartItem(models.Model):
    PRODUCT_TYPE_CHOICES = [
        ("tire", "Шина"),
        ("disk", "Диск"),
        ("akb", "Аккумулятор"),
    ]

    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name="items",
    )
    product_type = models.CharField(
        max_length=10,
        choices=PRODUCT_TYPE_CHOICES,
    )
    product_id = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField(default=1)
    price = models.IntegerField(verbose_name="Цена за единицу")

    class Meta:
        verbose_name = "Позиция корзины"
        verbose_name_plural = "Позиции корзины"

    def __str__(self):
        return f"{self.product_type} #{self.product_id} x {self.quantity}"

    @property
    def total_price(self):
        return self.price * self.quantity

    def get_product(self):
        """
        Возвращает объект товара (Tire / Disk / Akb) из соответствующей модели.
        Если товар уже удалён из базы — возвращает None.
        """
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
            return model.objects.get(pk=self.product_id)
        except model.DoesNotExist:
            return None

    @property
    def product(self):
        return self.get_product()
