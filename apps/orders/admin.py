from django.contrib import admin

from apps.orders.models import CartItem, Cart

admin.site.register(Cart)
admin.site.register(CartItem)