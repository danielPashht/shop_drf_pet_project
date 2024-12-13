from django.db import models
from category.models import Category


class Product(models.Model):
    discount_choices = [(i, i) for i in range(5, 100, 5)]
    discount = models.PositiveIntegerField(choices=discount_choices, default=0)
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_discounted_price(self, original_price):
        return original_price * (1 - self.discount / 100)

