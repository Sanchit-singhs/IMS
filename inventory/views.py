from django.shortcuts import render, get_object_or_404,redirect
from .models import User_s
from .forms import PostForm

# Create your views here.
def home(request):
    inventories = User_s.objects.all()
    return render(request, 'inventory/home.html', {'inventories':inventories})

def user_detail(request, pk):
    inventory = get_object_or_404(User_s, pk=pk)
    return render(request, 'inventory/user_detail.html', {'post': inventory})

def add_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            
            post.first_name = form.cleaned_data['first_name']
            post.last_name = form.cleaned_data['last_name']
            post.email = form.cleaned_data['email']
            post.phone_number = form.cleaned_data['phone_number']
            post.address = form.cleaned_data['address']
            post.save()
            return redirect('user_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'inventory/user_edit.html', {'form': form})