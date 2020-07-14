from django.contrib import admin
from .models import Category, Product, Property, ProductProperty, CategoryKeyProperty

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Property)
admin.site.register(ProductProperty)
admin.site.register(CategoryKeyProperty)
