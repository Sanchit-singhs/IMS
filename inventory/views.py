from django.shortcuts import render, get_object_or_404
from .models import User_s

# Create your views here.
def home(request):
    inventories = User_s.objects.all()
    return render(request, 'inventory/home.html', {'inventories':inventories})

def user_detail(request, pk):
    inventory = get_object_or_404(User_s, pk=pk)
    return render(request, 'inventory/user_detail.html', {'post': inventory})