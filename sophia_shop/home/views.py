from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView, View
from cart.cart import Cart
from .models import Product, UserProfile, CheckoutAddress
from .forms import NewUserForm, CheckoutForm

# Create your views here.

# Core views


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


# User creation
def logout_user(request):
    logout(request)
    messages.success(request, "Logout Successful")
    return redirect('index')


def register_user(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, ("Registration Complete"))
            return redirect('/')
        messages.error(
            request, "Error: Registration Unsuccessful. Invalid Information")
    form = NewUserForm()
    return render(request, 'users/register_user.html', {
        'register_form': form,
    })

# UserProfile managment


class UserProfileDetailView(DetailView):
    model = UserProfile
    template_name = "core/userprofile_detail.html"


class UserProfileListView(ListView):
    model = UserProfile
    template_name = "core/userprofile_list.html"


class UserProfileCreateView(CreateView):
    model = UserProfile
    template_name = "core/userprofile_create.html"


class UserProfileUpdateView(UpdateView):
    model = UserProfile
    template_name = "core/userprofile_update.html"


class UserProfileDeleteView(DeleteView):
    model = UserProfile
    template_name = "core/userprofile_delete.html"


# Shopping Cart
@login_required(login_url="/users/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect('shop')


@login_required(login_url="/users/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')

# Checkout views


class CheckoutView(View):
    def get(self, *args, **kwargs):
        form = CheckoutForm()
        context = {
            'form': form
        }
        return render(self.request, 'checkout.html', context)

    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)

        try:
            order = Cart.objects.get(user=self.request.user, ordered=False)
            if form.is_valid():
                street_address = form.cleaned_data.get('street_address')
                apartment_address = form.cleaned_data.get('apartment_address')
                country = form.cleaned_data.get('country')
                zip = form.cleaned_data.get('zip')
                same_billing_address = form.cleaned_data.get(
                    'same_billing_address')
                save_info = form.cleaned_data.get('save_info')
                payment_option = form.cleaned_data.get('payment_option')

                checkout_address = CheckoutAddress(
                    user=self.request.user,
                    street_address=street_address,
                    apartment_address=apartment_address,
                    country=country,
                    zip=zip
                )
                checkout_address.save()
                order.checkout_address = checkout_address
                order.save()
                return redirect('checkout')
            messages.warning(self.request, "Failed Chekout")
            return redirect('checkout')

        except ObjectDoesNotExist:
            messages.error(self.request, "You do not have an order")
            return redirect("order-summary")
