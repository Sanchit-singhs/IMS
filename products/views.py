from django.shortcuts import render
from .models import product

# Create your views here.
def product_list(request):
    products = product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})