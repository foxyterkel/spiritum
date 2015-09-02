from django.contrib import admin

# Register your models here.
from apps.product.models import Category, Brand, Product

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product)
