import uuid
from decimal import Decimal
from django.contrib import messages
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Category, Order, OrderItem, Product

def _cart(request):
    return request.session.get('cart', {})

def _cart_items(request):
    cart = _cart(request)
    products = Product.objects.filter(id__in=cart.keys())
    return [(product, int(cart[str(product.id)])) for product in products]

def home(request):
    return render(request, 'home.html', {'products': Product.objects.filter(is_featured=True).select_related('category'), 'categories': Category.objects.all()})

@require_POST
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart = _cart(request)
    key = str(product.id)
    cart[key] = min(int(cart.get(key, 0)) + 1, product.stock)
    request.session['cart'] = cart
    messages.success(request, f'{product.name} added to your kit.')
    return redirect(request.POST.get('next') or 'home')

@require_POST
def remove_from_cart(request, product_id):
    cart = _cart(request); cart.pop(str(product_id), None); request.session['cart'] = cart
    return redirect('cart')

def cart_detail(request):
    items = _cart_items(request)
    return render(request, 'cart.html', {'items': items, 'total': sum((p.price*q for p,q in items), Decimal('0'))})

def cart_count(request):
    return JsonResponse({'count': sum(int(quantity) for quantity in _cart(request).values())})

@transaction.atomic
def checkout(request):
    items = _cart_items(request)
    if not items: return redirect('home')
    total = sum((p.price*q for p,q in items), Decimal('0'))
    if request.method == 'POST':
        email = request.POST.get('email', '').strip(); address = request.POST.get('address', '').strip()
        if not email or not address:
            return render(request, 'checkout.html', {'items': items, 'total': total, 'error': 'Please complete your email and delivery address.'})
        order = Order.objects.create(order_number=f'FNS-{uuid.uuid4().hex[:8].upper()}', email=email, shipping_address=address, total_price=total)
        for product, quantity in items:
            OrderItem.objects.create(order=order, product=product, quantity=quantity, price_at_order=product.price)
            product.stock = max(0, product.stock - quantity); product.save(update_fields=['stock'])
        request.session['cart'] = {}
        return redirect('order_confirmation', order_number=order.order_number)
    return render(request, 'checkout.html', {'items': items, 'total': total})

def order_confirmation(request, order_number):
    return render(request, 'confirmation.html', {'order': get_object_or_404(Order, order_number=order_number)})

# Create your views here.
