from django.db import models

# Create your models here.


class Product(models.Model):
    prod_desc = models.CharField(max_length=200)
    prod_price = models.DecimalField(decimal_places=2, max_digits=5)
    date_added = models.DateTimeField("date added")
