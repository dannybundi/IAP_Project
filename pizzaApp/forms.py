# Forms.py

from django import forms

class OrderForm(forms.Form):
    name = forms.CharField(max_length=100)
    address = forms.CharField(widget=forms.Textarea)
    pizza_size = forms.ChoiceField(choices=[
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large'),
    ])
    quantity = forms.IntegerField(min_value=1)
