from django import forms
from product.models import Product



class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['productName','price','pictureProduct','description','categories'] #'__all__'
