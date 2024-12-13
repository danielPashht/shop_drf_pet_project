from django.contrib import admin
from .models import Order, OrderItem


class OrderAdmin(admin.ModelAdmin):
	list_display = ['id', 'user', 'order_status', 'total', 'created_at']
	list_filter = ['user']


class OrderItemAdmin(admin.ModelAdmin):
	list_display = ['order', 'product', 'quantity', 'price']
	list_filter = ['order', 'product']


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
