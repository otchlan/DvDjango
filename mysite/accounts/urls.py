from django.conf,urls import url
from . import views
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path


    urlpatterns = [

        path('login/', LoginView.as_view(template_name='login.html'), name="login"),
        path('logout/', LogoutView.as_view(template_name='logout.html'), name="logout"),
        path('register/', views.register, name='register'),
        path('profile/', views.profile, name='profile'),
    ]