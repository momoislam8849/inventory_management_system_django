from django import forms
from .models import Stock

class StockCreateForm(forms.ModelForm):
   class Meta:
     model = Stock
     fields = ['category', 'item_name', 'quantity']
     widgets = {
			'category': forms.TextInput(attrs={'class':'form-control','placeholder':'Category name'}),
			'item_name': forms.TextInput(attrs={'class':'form-control','placeholder':'Item name'}),
			'quantity': forms.TextInput(attrs={'class':'form-control'}),
			}

class StockSearchForm(forms.ModelForm):
   class Meta:
     model = Stock
     fields = ['item_name']

		