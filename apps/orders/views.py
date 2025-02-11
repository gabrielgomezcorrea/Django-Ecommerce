from django.shortcuts import get_object_or_404, redirect, render
from apps.cart.models import Cart
from apps.orders.forms import OrderCreateForm
from apps.orders.models import Order, OrderItem

# Create your views here.


def order_create(request):
    cart = None
    cart_id = request.session.get("cart_id")

    if cart_id:
        cart = Cart.objects.get(id=cart_id)

        if not cart or not cart.items.exists():
            return redirect("cart:cart_detail")

    if request.method == "POST":
        form = OrderCreateForm(request.POST)

        if form.is_valid():
            order = form.save(commit=False)
            order.save()

            for item in cart.items.all():
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    price=item.product.price,
                    quantity=item.quantity,
                )

            cart.delete()
            request.session["cart_id"] = None
            return redirect("orders:order_confirmation", order.id)
    else:
        form = OrderCreateForm()
        return render(request, "orders/order_create.html", {"cart": cart, "form": form})


def order_confirmation(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, "orders/order_confirmation.html", {"order": order})
