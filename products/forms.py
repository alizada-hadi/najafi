from django import forms
from .models import Buy, Product,Sale
from django.forms import modelformset_factory

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        exclude = ['total_price']
class BuyForm(forms.ModelForm):
    class Meta:
        model = Buy
        fields = '__all__'
        exclude = ["total_amount", "remined_amount"]
       

class  SaleForm (forms.ModelForm):
    class Meta:
        model = Sale
        fields = "__all__"




