# core/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegistrationForm
from .models import Technician, Shop, Product

# --- AUTH & HOME ---

def home(request):
    return render(request, 'core/index.html')

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'core/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'core/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

# --- LISTING PAGES ---

def technicians_view(request):
    technicians = Technician.objects.select_related('user').prefetch_related('skills').all()
    return render(request, 'core/technicians.html', {'technicians': technicians})

def shops_view(request):
    shops = Shop.objects.select_related('user').all()
    return render(request, 'core/shops.html', {'shops': shops})

def products_view(request):
    products = Product.objects.select_related('shop', 'category').all()
    return render(request, 'core/products.html', {'products': products})

# --- NAVIGATION PAGES ---

def services_view(request):
    return render(request, 'core/services.html')

def how_it_works_view(request):
    return render(request, 'core/how_it_works.html')

def providers_view(request):
    return render(request, 'core/providers.html')

def about_view(request):
    return render(request, 'core/about.html')

def contact_view(request):
    if request.method == 'POST':
        # Handle contact form submission
        name = request.POST.get('name')
        return render(request, 'core/contact_success.html', {'name': name})
    return render(request, 'core/contact.html')

def contact_success_view(request):
    return render(request, 'core/contact_success.html')