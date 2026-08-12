# core/admin.py
from django.contrib import admin
from .models import (
    User, Skill, Technician, Shop, Category, 
    Product, Appointment, Order, OrderItem, Review
)

# Register all models
admin.site.register(User)
admin.site.register(Skill)
admin.site.register(Technician)
admin.site.register(Shop)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Appointment)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Review)