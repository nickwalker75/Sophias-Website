import uuid
from django.db import models
from home.models import Customer, Category

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200,
                             default="Product Title")
    description = models.CharField(max_length=200,
                                   default="Product Description")
    price = models.DecimalField(decimal_places=2, max_digits=6,
                                default=0.00)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to='uploads/products/', default='')
    is_avaliable = models.BooleanField(default=True)

    # Product on sale
    on_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(
        decimal_places=2, max_digits=6, default=0.00)

    def __str__(self):
        return self.title
    
