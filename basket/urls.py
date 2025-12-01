from django.urls import path

from . import views

app_name = "basket"

urlpatterns = [
    path("", views.cart_detail, name="cart_detail"),
    path("add/<str:product_type>/<int:pk>/", views.add_to_cart, name="add_to_cart"),
    path("remove/<int:item_id>/", views.remove_from_cart, name="remove_from_cart"),
    path("change-quantity/<int:item_id>/", views.change_quantity, name="change_quantity"),
]
