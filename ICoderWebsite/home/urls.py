"""ICoder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="Home Page"),
    path('contact', views.contact, name="Contact Page"),
    path('about', views.about, name="About Page"),
    path('search', views.search, name="Search Page"),
    path('signup', views.handlesignup, name="Sign Up Form"),
    path('signin', views.handlelogin, name="Sign In Form"),
    path('logout', views.handlelogout, name="Logout Page")

]
