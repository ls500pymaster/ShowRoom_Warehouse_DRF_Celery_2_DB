from django import forms
from .models import CartItem, Car

class CartItemForm(forms.ModelForm):
    car = forms.ModelChoiceField(queryset=Car.objects.all(), empty_label=None)

    class Meta:
        model = CartItem
        fields = ['car', 'quantity']
