from django.db import models
import datetime
import uuid

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=50)
    pwrd = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.user_name}'


# Product Categories
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'


# Products
class Product(models.Model):
    title = models.CharField(max_length=200,
                             default="Product Title")
    description = models.CharField(max_length=200,
                                   default="Product Description")
    price = models.DecimalField(decimal_places=2, max_digits=6,
                                default=0.00)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to='uploads/products/', default='')

    # Product on sale
    on_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(
        decimal_places=2, max_digits=6, default=0.00)

    def __str__(self):
        return self.title


# Customer Orders
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address = models.CharField(max_length=75, default='', blank=False)
    phone = models.CharField(max_length=20, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    shipping_status = models.BooleanField(default=False)
    orderNum = models.CharField(
        max_length=100, blank=True, unique=True, default=uuid.uuid4)

    def __str__(self):
        return self.orderNum
