from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'price', 'category', 'id', 'discount'
    )
    search_fields = ('title', 'category', 'id')


admin.site.register(Product, ProductAdmin)
