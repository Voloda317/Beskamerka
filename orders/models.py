from django.db import models
from django.contrib.auth.models import User

from tires.models import Tire
from disks.models import Disk
from akb.models import Akb


class Order(models.Model):
    STATUS_ORDERS = [
        ("new", "новый"),
        ("processing", "в обработке"),
        ("shipped", "отправлен"),
        ("delivered", "доставлен"),
        ("canceled", "отменён"),
        ("returned", "возвращён"),
        ("completed", "завершён"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="orders",
        verbose_name="Пользователь",
    )
    phone = models.CharField("Телефон", max_length=20, blank=True)

    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField("Дата обновления", auto_now=True)

    status = models.CharField(
        "Статус",
        max_length=20,
        choices=STATUS_ORDERS,
        default="new",
    )

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        ordering = ["-created_at"]

    def __str__(self):
        return f"Заказ #{self.pk}"

    @property
    def total_price(self):
        return sum(item.total_price for item in self.items.all())


class OrderItem(models.Model):
    PRODUCT_TYPE_CHOICES = [
        ("tire", "Шина"),
        ("disk", "Диск"),
        ("akb", "Аккумулятор"),
    ]

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="items",
        verbose_name="Заказ",
    )
    product_type = models.CharField(
        "Тип товара",
        max_length=10,
        choices=PRODUCT_TYPE_CHOICES,
    )
    product_id = models.PositiveIntegerField("ID товара в своей таблице")
    product_name = models.CharField("Название товара", max_length=255)
    # НОВОЕ ПОЛЕ — артикул товара
    product_art = models.CharField("Артикул", max_length=70, blank=True, null=True)

    quantity = models.PositiveIntegerField("Кол-во", default=1)
    price = models.IntegerField("Цена за единицу")

    class Meta:
        verbose_name = "Позиция заказа"
        verbose_name_plural = "Позиции заказа"

    def __str__(self):
        return f"{self.product_name} x {self.quantity}"

    @property
    def total_price(self):
        return self.quantity * self.price

    def get_product(self):
        """
        Возвращает объект товара (Tire / Disk / Akb).
        Можно использовать в админке или в шаблонах.
        """
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
