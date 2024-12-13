from django.db import models


class Cart(models.Model):
	user = models.OneToOneField(
		"users.User",
		on_delete=models.CASCADE,
		related_name="user_cart"
	)
	products = models.ManyToManyField("products.Product", through="CartProduct")
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"Cart for {self.user}"


class CartProduct(models.Model):
	cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
	product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
	quantity = models.PositiveIntegerField(default=1)

	def __str__(self):
		return f"{self.product.title} (x{self.quantity}) in cart for {self.cart.user}"
