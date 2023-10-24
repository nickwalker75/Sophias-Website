from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Product Categories
class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"pk": self.pk})

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
    
    TVA_AMOUNT = 19.25

    def price_ttc(self):
        return self.price_ht + self.TVA_AMOUNT

    def __str__(self):
        return self.name		

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"pk": self.pk})

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profile_images', blank=True)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.user + "profile"

    def get_absolute_url(self):
        return reverse("profile_detail", kwargs={"pk": self.pk})



