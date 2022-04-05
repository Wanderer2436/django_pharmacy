from django import forms
from basket.models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
