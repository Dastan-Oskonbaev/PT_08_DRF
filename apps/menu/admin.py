from django.contrib import admin

from apps.menu.models import Product, Category, Article, Post, Tag

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Post)
admin.site.register(Tag)