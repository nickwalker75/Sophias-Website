import uuid
from django.db import models
from home.models import Customer, Product

# Create your models here.


class Cart(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)


class CartItem(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="products")
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name="cartItems")
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return str(self.product.title)
