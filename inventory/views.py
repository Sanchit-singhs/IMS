from django.shortcuts import render
from .models import User_s

# Create your views here.
def home(request):
    inventories = User_s.objects.all()
    return render(request, 'inventory/home.html', {'inventories':inventories})