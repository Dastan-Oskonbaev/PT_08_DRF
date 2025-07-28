from django.db import models

from apps.menu.models import Product
from apps.users.models import CustomUser


class Cart(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.first_name} Cart'

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


    def __str__(self):
        return f'{self.product.name} in {self.cart.user.first_name} cart'