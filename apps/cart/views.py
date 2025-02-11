from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from apps.cart.models import Cart, CartItem
from apps.products.models import Product

# Create your views here.


def cart_details(request):
    cart_id = request.session.get("cart_id")
    cart = None

    if cart_id:
        cart = get_object_or_404(Cart, id=cart_id)

    return render(
        request,
        "cart/details.html",
        {
            "cart": cart,
        },
    )


@require_POST
def cart_add(request, product_id):
    cart_id = request.session.get("cart_id")

    if not cart_id:
        cart = Cart.objects.create()
        request.session["cart_id"] = cart.id
    else:
        try:
            cart = Cart.objects.get(id=cart_id)
        except Cart.DoesNotExist:
            cart = Cart.objects.create()
            request.session["cart_id"] = cart.id

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
    cart = get_object_or_404(Cart, id=cart_id)
    item = get_object_or_404(CartItem, cart=cart, product_id=product_id)
    item.delete()

    return redirect("cart:cart_details")
