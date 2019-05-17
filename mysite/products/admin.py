from django.contrib import admin

from products.models import Product, SuperProduct

admin.site.register(Product)
admin.site.register(SuperProduct)