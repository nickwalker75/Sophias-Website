from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

# Core urls
urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("shop/", views.shop, name="shop"),
]

# User Urls
urlpatterns += [
    path("login_user/", views.login_user, name="login"),
    path("logout_user/", views.logout_user, name="logout"),
    path("register_user/", views.register_user, name="register"),
    path('profiles/', views.UserProfileListView.as_view(), name='profile-list'),
    path('profile/<int:pk>/', views.UserProfileDetailView.as_view(),
         name='profile-detail'),
    path('profile/create/', views.UserProfileCreateView.as_view(),
         name='profile-create'),
    path('profile/<int:pk>/update/',
         views.UserProfileUpdateView.as_view(), name='profile-update'),
    path('profile/<int:pk>/delete/',
         views.UserProfileDeleteView.as_view(), name='profile-delete'),
]

# Shopping cart Urls
urlpatterns += [
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/', views.cart_detail, name='cart_detail'),
]

# Checkout Urls
# urlpatterns += [
#    path('checkout', views.CheckoutView.as_view(), name='checkout')
# ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
