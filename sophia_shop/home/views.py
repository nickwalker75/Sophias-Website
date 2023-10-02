from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.


def index(request):
    return render(request, "home/index.html", {})


def shop(request):
    products = Product.objects.all()
    return render(request, "home/shop.html", {'products': products})


def checkout(request):
    return render(request, "home/checkout.html", {})


def cart(request):
    return render(request, "home/cart.html", {})


def about(request):
    return render(request, "home/about.html", {})
