# Views.py

from django.shortcuts import render
from .forms import OrderForm

def home(request):
    return render(request, 'pizza/home.html')

def order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            return render(request, 'pizza/thanks.html', {'name': form.cleaned_data['name']})
    else:
        form = OrderForm()
    return render(request, 'pizza/order.html', {'form': form})
