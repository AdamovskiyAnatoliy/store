from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

from betterforms.multiform import MultiModelForm

from .models import Product

class ProductForm(ModelForm):

    class Meta:
        model = Product
        fields = (
            'name_product', 'detail', 'type_of_product', 'pub_date',
            'photo',
        )
