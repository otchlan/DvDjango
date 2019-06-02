"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView , LogoutView
from mysite import views

from pages.views import home_view,about_view,base_view, contact_view, test_view, index_view, main_view

from products.views import product_detail_view, super_product_detail_view
from accounts.views import register_view


app_name = "users"

urlpatterns = [
    path(r'^$', views.login_redirect, name='login_redirect'),
    path('', home_view, name='home'),
    path('about/',about_view),
    path('home/' , home_view),
    path('admin/', admin.site.urls),
    path('base/', base_view),
    path('contact/', contact_view),
    path('test/', test_view),
    path('index/', index_view),
    path('main/', main_view),
    path('login/', LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name="logout"),
    path('products/', product_detail_view),
    path('register/', register_view),


]
