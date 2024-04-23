from .views import *
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', home, name='home'),
    path('client', client, name='client'),
    path('client_edit', client_edit, name='client_edit'),
    path('perfomancer',perfomancer, name='perfomancer'),
    path('performer_edit',perfomancer_edit, name='performer_edit'),
    path('register',registration, name='register'),
    path('login',login_view, name='login'),
    path('logout',logout_view, name='logout'),
]
