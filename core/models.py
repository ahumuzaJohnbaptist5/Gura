# core/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

# 1. USERS
class User(AbstractUser):
    ROLE_CHOICES = (
        ('CUSTOMER', 'Customer'),
        ('TECHNICIAN', 'Technician'),
        ('SHOP_OWNER', 'Shop Owner'),
        ('ADMIN', 'Admin'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='CUSTOMER')
    phone = models.CharField(max_length=15, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.role})"

# 2. SKILLS
class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

# 3. TECHNICIANS
class Technician(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='technician_profile')
    bio = models.TextField()
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2)
    skills = models.ManyToManyField(Skill, related_name='technicians')
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)

    def __str__(self):
        return f"Tech: {self.user.username}"

# 4. SHOPS
class Shop(models.Model):
    SHOP_TYPE_CHOICES = (
        ('REPAIR', 'Repair Shop'),
        ('ELECTRONICS', 'Electronics Shop'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='shop_profile')
    name = models.CharField(max_length=200)
    shop_type = models.CharField(max_length=20, choices=SHOP_TYPE_CHOICES)
    address = models.CharField(max_length=255)
    description = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)

    def __str__(self):
        return self.name

# 5. CATEGORIES
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

# 6. PRODUCTS
class Product(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='products')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.name