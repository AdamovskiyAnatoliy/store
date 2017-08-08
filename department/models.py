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
    name_product = models.CharField(max_length=50)
    detail = models.TextField()
    type_of_product = models.CharField(max_length=2, choices=TYPE_OF_PERODUCT)
    pub_date = models.DateTimeField(default=timezone.now)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    priсe = models.DecimalField(max_digits=9, decimal_places=2)
    like = models.PositiveIntegerField(default=0)
    dislike = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name_product


class User(models.Model):
    ban = models.BooleanField(default=False)
    pub_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=4, decimal_places=2)
    phone_number = models.PositiveIntegerField(blank=True)

    def cost_of_desires(self):
        pass

    def up_user_rating(self):
        self.rating =+ 1
        self.save()
        return ''
