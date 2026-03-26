from django.http import HttpResponseBadRequest
from django.shortcuts import redirect, render
from django.urls import reverse

from .models import Contact


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def menu(request):
    return render(request, "menu.html")


def food(request):
    return render(request, "food.html")


def order(request):
    return render(request, "order.html")


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,
        )

        # Reload page after submit
        return redirect("contact")

    return render(request, "contact.html")


def combo(request):
    return render(request, "combo.html")


# Static catalog for UI-only ordering (no DB-backed products yet).
# Keys must match the item_key used in templates.
CATALOG = {
    # Menu (Chai)
    "masala-chai": {"name": "Masala Chai", "price": 20},
    "ginger-chai": {"name": "Ginger Chai", "price": 25},
    "elaichi-chai": {"name": "Elaichi Chai", "price": 25},
    "cutting-chai": {"name": "Cutting Chai", "price": 15},
    "chocolate-chai": {"name": "Chocolate Chai", "price": 35},
    "kashmiri-kahwa": {"name": "Kashmiri Kahwa", "price": 50},

    # Food
    "samosa": {"name": "Samosa", "price": 15},
    "pakoda": {"name": "Pakoda", "price": 20},
    "kachori": {"name": "Kachori", "price": 25},
    "dhokla": {"name": "Dhokla", "price": 30},
    "vada-pav": {"name": "Vada Pav", "price": 20},
    "bhelpuri": {"name": "Bhelpuri", "price": 35},

    # Combo
    "classic-duo": {"name": "Classic Duo", "price": 40},
    "monsoon-magic": {"name": "Monsoon Magic", "price": 50},
    "mumbai-special": {"name": "Mumbai Special", "price": 45},
    "gujarati-treat": {"name": "Gujarati Treat", "price": 65},
    "royal-feast": {"name": "Royal Feast", "price": 75},
    "light-bite": {"name": "Light Bite", "price": 60},
}


def _get_cart(session):
    cart = session.get("cart", {})
    # Normalize to {str: int}
    normalized = {}
    for k, v in cart.items():
        try:
            qty = int(v)
        except (TypeError, ValueError):
            qty = 0
        if qty > 0:
            normalized[str(k)] = qty
    return normalized


def cart_view(request):
    cart = _get_cart(request.session)
    items = []
    total = 0
    for item_key, qty in cart.items():
        item = CATALOG.get(item_key)
        if not item:
            continue
        line_total = item["price"] * qty
        items.append(
            {
                "key": item_key,
                "name": item["name"],
                "price": item["price"],
                "qty": qty,
                "line_total": line_total,
            }
        )
        total += line_total

    return render(request, "cart.html", {"items": items, "total": total})


def cart_add(request, item_key: str):
    if item_key not in CATALOG:
        return HttpResponseBadRequest("Invalid item")

    cart = _get_cart(request.session)
    cart[item_key] = cart.get(item_key, 0) + 1
    request.session["cart"] = cart

    # Go back to the page the user came from
    referer = request.META.get("HTTP_REFERER")
    return redirect(referer or reverse("cart"))


def cart_update(request, item_key: str):
    if item_key not in CATALOG:
        return HttpResponseBadRequest("Invalid item")

    if request.method != "POST":
        return HttpResponseBadRequest("Invalid method")

    qty_raw = request.POST.get("qty", "0")
    try:
        qty = int(qty_raw)
    except ValueError:
        qty = 0

    cart = _get_cart(request.session)
    if qty <= 0:
        cart.pop(item_key, None)
    else:
        cart[item_key] = qty
    request.session["cart"] = cart

    return redirect(reverse("cart"))


def cart_remove(request, item_key: str):
    if item_key not in CATALOG:
        return HttpResponseBadRequest("Invalid item")

    cart = _get_cart(request.session)
    cart.pop(item_key, None)
    request.session["cart"] = cart
    return redirect(reverse("cart"))


def cart_checkout(request):
    cart = _get_cart(request.session)
    if not cart:
        return redirect(reverse("cart"))

    items = []
    total = 0
    for item_key, qty in cart.items():
        item = CATALOG.get(item_key)
        if not item:
            continue
        line_total = item["price"] * qty
        items.append(
            {
                "key": item_key,
                "name": item["name"],
                "price": item["price"],
                "qty": qty,
                "line_total": line_total,
            }
        )
        total += line_total

    if request.method == "POST":
        # For now we just clear the cart (no DB Order model in this project yet).
        request.session["cart"] = {}
        return render(request, "checkout_success.html")

    return render(request, "checkout.html", {"items": items, "total": total})
