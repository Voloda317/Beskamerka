from .models import Cart


def get_cart(request):
    """Получаем (или создаём) корзину по session_key."""
    session_key = request.session.session_key
    if not session_key:
        request.session.create()
        session_key = request.session.session_key

    cart, _ = Cart.objects.get_or_create(session_key=session_key)
    return cart
