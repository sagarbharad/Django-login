from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from .views import login, signup, home, logout_user
urlpatterns = [
    path('login', login),  
    path('', login),  
  
    path('profile', home),
    path('signup', signup),
    path('logout_user', logout_user),


]
