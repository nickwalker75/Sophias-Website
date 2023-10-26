from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User
from django_countries.fields import CountryField
import uuid

# Product Models
class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200,
                             default="Product Title")
    description = models.CharField(max_length=200,
                                   default="Product Description")
    price = models.FloatField(default=0.00)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to='uploads/products/', default='')
    is_avaliable = models.BooleanField(default=True)

    # Product on sale
    on_sale = models.BooleanField(default=False)
    sale_price = models.FloatField(blank=True)

    def __str__(self):
        return self.name		

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"pk": self.pk})


# User Models
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profile_images', blank=True)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.user + "profile"

    def get_absolute_url(self):
        return reverse("profile_detail", kwargs={"pk": self.pk})



# Checkout Models
class CheckoutAddress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100)
    country = CountryField(multiple=False)
    zip = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username