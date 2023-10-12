from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, "index.html", {})


def shop(request):
    products = Product.objects.all()
    return render(request, "shop.html", {'products': products})


def checkout(request):
    return render(request, "checkout.html", {})


def cart(request):
    return render(request, "shopping_cart/cart.html", {})


def about(request):
    return render(request, "about.html", {})


def login_user(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            messages.success(
                request, ("Success"))
            return redirect('/')
        else:
            # Return an 'invalid login' error message.
            messages.success(
                request, ("ERROR: Incorrect Username or Password"))
            return redirect('/login_user')

    else:
        return render(request, 'users/login_user.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, "Logout Successful")
    return redirect('index')


def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data('username')
            password = form.cleaned_data('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration Complete"))
            return redirect('/')
        else:
            form = UserCreationForm()
    return render(request, 'users/register_user.html', {
        'form': form,
    })
