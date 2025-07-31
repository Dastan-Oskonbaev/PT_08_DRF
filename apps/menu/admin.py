from django.contrib import admin

from apps.menu.models import Product, Category, Article

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Article)