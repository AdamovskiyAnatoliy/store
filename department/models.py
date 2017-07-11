from django.db import models
from django.utils import timezone


class Product(models.Model):
    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=50)
    detail = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
    priсe = models.DecimalField(max_digits=9, decimal_places=2)
    in_basket = models.BooleanField(default=False)
    like = models.PositiveIntegerField(default=0)
    dislike = models.PositiveIntegerField(default=0)


class User(models.Model):
    desire = models.ForeignKey(Product)
    ban = models.BooleanField(default=False)

#add def Sub-market prices
