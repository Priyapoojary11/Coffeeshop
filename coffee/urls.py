from django.urls import path
# from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.login_view, name='root'),  # Redirect root URL to login
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('gallery/', views.gallery, name='gallery'),
    path('coffee/<int:coffee_id>/', views.view_coffee, name='view_coffee'),  # URL for viewing specific coffee,
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('add_to_checkout/<int:product_id>/', views.add_to_checkout, name='add_to_checkout'),
    path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('view_cart/', views.view_cart, name='view_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('checkout1/', views.checkout1, name='checkout1'),
    path('payment/<int:order_id>/', views.payment, name='payment'),
    path('profile/', views.profile, name='profile'),
]
