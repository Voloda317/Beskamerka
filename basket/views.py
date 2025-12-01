from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from tires.models import Tire
from disks.models import Disk
from akb.models import Akb

from .models import CartItem
from .utils import get_cart


def cart_detail(request):
    """Страница корзины."""
    cart = get_cart(request)
    items = cart.items.select_related()  # CartItem
    context = {
        "cart": cart,
        "items": items,
    }
    return render(request, "basket/cart.html", context)


@require_POST
def add_to_cart(request, product_type, pk):
    """
    Добавить товар в корзину.
    product_type: 'tire' | 'disk' | 'akb'
    pk: id товара
    """
    cart = get_cart(request)

    model_map = {
        "tire": Tire,
        "disk": Disk,
        "akb": Akb,
    }
    model = model_map.get(product_type)
    if not model:
        return redirect("homepage:home")  # на всякий случай

    product = get_object_or_404(model, pk=pk)

    # пробуем найти уже существующую позицию
    item, created = CartItem.objects.get_or_create(
        cart=cart,
        product_type=product_type,
        product_id=product.id,
        defaults={"quantity": 1, "price": product.price},
    )
    if not created:
        item.quantity += 1
        item.save()

    # можно вернуть на страницу, с которой пришли
    next_url = request.POST.get("next") or request.META.get("HTTP_REFERER") or "/"
    return redirect(next_url)


@require_POST
def remove_from_cart(request, item_id):
    """Удалить позицию из корзины."""
    cart = get_cart(request)
    item = get_object_or_404(CartItem, id=item_id, cart=cart)
    item.delete()
    next_url = request.POST.get("next") or request.META.get("HTTP_REFERER") or "/basket/"
    return redirect(next_url)


@require_POST
def change_quantity(request, item_id):
    """Изменить количество позиции в корзине."""
    cart = get_cart(request)
    item = get_object_or_404(CartItem, id=item_id, cart=cart)

    try:
        quantity = int(request.POST.get("quantity", 1))
    except (TypeError, ValueError):
        quantity = 1

    if quantity <= 0:
        item.delete()
    else:
        item.quantity = quantity
        item.save()

    next_url = request.POST.get("next") or request.META.get("HTTP_REFERER") or "/basket/"
    return redirect(next_url)
