from django import forms
import core.models


class ProductEdit(forms.ModelForm):
    class Meta:
        model = core.models.Product
        fields = '__all__'
