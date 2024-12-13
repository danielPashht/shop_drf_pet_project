import uuid
from django.db import models
from products.models import Product


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    STATUS_CHOICES = [
        ('pending', 'Pending'),  # Order created but not paid
        ('processing', 'Processing'),  # Order paid and about to ship
        ('shipped', 'Shipped'),  # Order shipped
        ('completed', 'Completed'),  # Order received
        ('canceled', 'Canceled'),
    ]
    order_status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='pending')
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Product, through='OrderItem')

    def __str__(self):
        return f"Order {self.id}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.product.title} (x{self.quantity})"
