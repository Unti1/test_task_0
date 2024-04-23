from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Client, Performer, NavBar
from mptt.admin import MPTTModelAdmin


# Register your models here.

class ClientView(ModelAdmin): 
    list_display = ['user', 'rating']

class PerformerView(ModelAdmin):
    list_display = ['user', 'rating']

admin.site.register(Client, ClientView)
admin.site.register(Performer, PerformerView)
admin.site.register(NavBar)