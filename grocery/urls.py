"""grocery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.views.static import serve
from grocery import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.SignUpPage, name="signup"),
    path("login/",views.LoginPage, name="login"),
    path("home/",views.home, name="home"),
    path('logout/',views.LogoutPage,name="logout"),
    path('products/<int:product_id>/', views.Products, name='products'),
    path('products/', views.Products, name='all_products'),
    path('cart/', views.cart, name="cart" ),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name="add_to_cart" ),
    path('payment/',views.payment,name='payment'),
]

urlpatterns += staticfiles_urlpatterns()