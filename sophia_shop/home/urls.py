from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

# Core urls
urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("shop/", views.shop, name="shop"),
    path("cart/", views.cart, name="cart"),
    path("checkout/", views.checkout, name="checkout"),
    path("login_user/", views.login_user, name="login"),
    path("logout_user/", views.logout_user, name="logout"),
    path("register_user/", views.register_user, name="register"),
]

# UserProfile Urls
urlpatterns += [
    path('profiles/', views.UserProfileListView.as_view(), name='profile-list'),
    path('profile/<int:pk>/', views.UserProfileDetailView.as_view(), name='profile-detail'),
    path('profile/create/', views.UserProfileCreateView.as_view(), name='profile-create'),
    path('profile/<int:pk>/update/', views.UserProfileUpdateView.as_view(), name='profile-update'),
    path('profile/<int:pk>/delete/', views.UserProfileDeleteView.as_view(), name='profile-delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
