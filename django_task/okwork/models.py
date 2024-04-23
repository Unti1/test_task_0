from mptt.models import MPTTModel, TreeForeignKey
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db import models

# Create your models here.

class Client(models.Model):
    avatar = models.ImageField(upload_to='clients/avatars/')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=100)
    experience = models.JSONField(null=True)
    rating = models.FloatField(null=True)


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class Performer(models.Model):
    avatar = models.ImageField(upload_to='performers/avatars/')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=100)
    rating = models.FloatField(null=True)
    sell_categories = models.JSONField(null=True)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
    
class Order(models.Model):
    title = models.CharField(max_length=100)
    cost = models.FloatField()
    description = models.CharField(max_length=4096)

class NavBar(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    url_name = models.CharField(max_length=100)
    login_req = models.BooleanField(default=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name
    


@receiver(post_save, sender=User)
def create_user_client(sender, instance, created, **kwargs):
    if created:
        Client.objects.create(user=instance)

@receiver(post_save, sender=User)
def create_user_performer(sender, instance, created, **kwargs):
    if created:
        Performer.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_client(sender, instance, **kawrgs):
    instance.client.save()

@receiver(post_save, sender=User)
def save_user_performer(sender, instance, **kawrgs):
    instance.performer.save()