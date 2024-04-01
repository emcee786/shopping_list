from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={"class":"myinput", "placeholder":"Add item"}))
    class Meta:
        model = Item
        fields = ["title"]