from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from tires.models import Tire
from disks.models import Disk
from akb.models import Akb

from .models import CartItem
from .utils import get_cart
from django.contrib import messages
from orders.models import Order, OrderItem


def _get_product_model(product_type: str):
    """Возвращаем модель по типу товара."""
    return {
        "tire": Tire,
        "disk": Disk,
        "akb": Akb,
    }.get(product_type)


def cart_detail(request):
    """Страница корзины."""
    cart = get_cart(request)
    items = cart.items.all()
    total_price = sum(item.total_price for item in items)

    context = {
        "cart": cart,
        "items": items,
        "total_price": total_price,
    }
    return render(request, "basket/cart.html", context)


@require_POST
def add_to_cart(request, product_type, pk):
    """
    Добавление товара в корзину.
    product_type: 'tire' | 'disk' | 'akb'
    pk: ID товара в соответствующей таблице.
    """
    cart = get_cart(request)
    model = _get_product_model(product_type)

    if model is None:
        return redirect("basket:cart_detail")

    product = get_object_or_404(model, pk=pk)

    # количество из формы (по умолчанию 1)
    try:
        quantity = int(request.POST.get("quantity", "1"))
    except ValueError:
        quantity = 1
    if quantity < 1:
        quantity = 1

    item, created = CartItem.objects.get_or_create(
        cart=cart,
        product_type=product_type,
        product_id=product.pk,
        defaults={"price": getattr(product, "price", 0)},
    )

    if created:
        item.quantity = quantity
    else:
        item.quantity += quantity
        # обновляем цену, если она вдруг изменилась
        item.price = getattr(product, "price", item.price)
    item.save()

    # куда редиректить после добавления
    next_url = request.POST.get("next") or request.META.get("HTTP_REFERER")
    if next_url:
        return redirect(next_url)
    return redirect("basket:cart_detail")


@require_POST
def remove_from_cart(request, item_id):
    """Удалить позицию из корзины."""
    cart = get_cart(request)
    CartItem.objects.filter(id=item_id, cart=cart).delete()
    return redirect("basket:cart_detail")


@require_POST
def change_quantity(request, item_id):
    """Изменение количества позиции в корзине."""
    cart = get_cart(request)
    item = get_object_or_404(CartItem, id=item_id, cart=cart)

    try:
        quantity = int(request.POST.get("quantity", "1"))
    except ValueError:
        quantity = 1

    if quantity <= 0:
        item.delete()
    else:
        item.quantity = quantity
        item.save()

    return redirect("basket:cart_detail")


@require_POST
def checkout(request):
    """
    Оформление заказа: только для авторизованных пользователей.
    Анонимного пользователя отправляем на страницу входа с сообщением.
    """

    # если пользователь не залогинен — показываем уведомление и перекидываем
    if not request.user.is_authenticated:
        messages.warning(
            request,
            "Чтобы оформить заказ, вы должны быть зарегистрированы и войти в аккаунт."
        )
        return redirect("accounts:login")

    cart = get_cart(request)

    # если корзина пустая — просто вернём на страницу корзины
    if not cart.items.exists():
        messages.info(request, "Ваша корзина пуста.")
        return redirect("basket:cart_detail")

    user = request.user
    profile = getattr(user, "profile", None)

    # создаём заказ
    order = Order.objects.create(
        user=user,
        phone=profile.phone if profile else "",
    )

    # переносим позиции корзины в заказ
    for item in cart.items.all():
        product = item.product  # свойство из CartItem.get_product()

        if product is not None:
            product_name = str(product)
        else:
            # если товар уже удалён из каталога — всё равно что-то сохраним
            product_name = f"{item.product_type} #{item.product_id}"

        OrderItem.objects.create(
            order=order,
            product_type=item.product_type,
            product_id=item.product_id,
            product_name=product_name,
            quantity=item.quantity,
            price=item.price,
        )

    # очищаем корзину
    cart.items.all().delete()

    messages.success(request, f"Ваш заказ №{order.id} успешно оформлен!")
    return render(request, "basket/order_success.html", {"order": order})

