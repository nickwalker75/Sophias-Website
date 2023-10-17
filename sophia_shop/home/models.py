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




