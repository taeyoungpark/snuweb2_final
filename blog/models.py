from django.db import models
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
                return self.name

class Shop(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=40)
    address = models.CharField(max_length=500)
    description = models.TextField()
    photo1 = models.ImageField()
    photo2 = models.ImageField(null=True, blank=True)
    photo3 = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category)

    def __str__(self):
                return self.name

class Review(models.Model):
    shop = models.ForeignKey(Shop)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    comment = models.TextField()
    photo1 = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
                return self.pk
