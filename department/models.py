from django.db import models
from django.utils import timezone


class Product(models.Model):
    TYPE_OF_PERODUCT = (
        ('MB', 'Mobile'),
        ('LP', 'Laptop'),
        ('TB', 'Tablet'),
        ('CN', 'Consoles'),
    )
    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=50)
    detail = models.TextField()
    type_of_product = models.CharField(max_length=2, choice=TYPE_OF_PERODUCT)
    pub_date = models.DateTimeField(default=timezone.now)
    photo = models.ImageField(upload_to='image')
    priсe = models.DecimalField(max_digits=9, decimal_places=2)
    in_basket = models.BooleanField(default=False)
    like = models.PositiveIntegerField(default=0)
    dislike = models.PositiveIntegerField(default=0)


class User(models.Model):
    desire = models.ForeignKey(Product,  on_delete=models.CASCADE)
    ban = models.BooleanField(default=False)

    def cost_of_desires(self):
        pass


class Seller(models.Model):
    #name and date 
    pub_product = models.Foreignkey(Product, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=2, max_length=2)
    #phone_number = models.PositiveIntegerField()
