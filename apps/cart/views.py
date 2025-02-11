from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from apps.cart.models import Cart, CartItem
from apps.products.models import Product


def cart_details(request):
    cart_id = request.session.get("cart_id")

    if cart_id:
        cart = Cart.objects.filter(
            id=cart_id
        ).first()  # Usamos .filter().first() para evitar errores si no existe
    else:
        cart = None  # Si no hay cart_id en la sesión, el carrito es None

    return render(
        request,
        "cart/details.html",
        {"cart": cart},
    )


@require_POST
def cart_add(request, product_id):
    cart_id = request.session.get("cart_id")

    if not cart_id or not Cart.objects.filter(id=cart_id).exists():
        cart = Cart.objects.create()
        request.session["cart_id"] = cart.id
    else:
        cart = Cart.objects.get(id=cart_id)

    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return JsonResponse(
        {
            "cart_id": cart.id,
            "product_id": product.id,
            "quantity": cart_item.quantity,
        }
    )


@require_POST
def cart_remove_item(request, product_id):
    cart_id = request.session.get("cart_id")

    if not cart_id or not Cart.objects.filter(id=cart_id).exists():
        return redirect("cart:cart_details")  # Evita error si no hay carrito

    cart = Cart.objects.get(id=cart_id)
    item = get_object_or_404(CartItem, cart=cart, product_id=product_id)
    item.delete()

    return redirect("cart:cart_details")
