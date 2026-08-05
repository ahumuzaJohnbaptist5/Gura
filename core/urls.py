# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # Listing Pages
    path('technicians/', views.technicians_view, name='technicians'),
    path('shops/', views.shops_view, name='shops'),
    path('products/', views.products_view, name='products'),
    
    # New Navigation Pages
    path('services/', views.services_view, name='services'),
    path('how-it-works/', views.how_it_works_view, name='how_it_works'),
    path('providers/', views.providers_view, name='providers'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('contact/success/', views.contact_success_view, name='contact_success'),
]