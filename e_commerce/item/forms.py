from django import forms
from .models import Item

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['category','name','description','price','image']
        help_texts={
            'image':"Upload your item's image",
            'category':"Select your item's category",
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name','description','price','image','is_sold']
        help_texts={
            'image':"Upload your item's image",
        }