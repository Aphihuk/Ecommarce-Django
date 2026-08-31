from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=80)
    slug = models.SlugField(unique=True)
    icon = models.CharField(max_length=10, default='✦')
    def __str__(self): return self.name

class Product(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField(blank=True)
    tone = models.CharField(max_length=20, default='blue')
    tag = models.CharField(max_length=20, default='FNS PICK')
    stock = models.PositiveIntegerField(default=10)
    is_featured = models.BooleanField(default=True)
    def __str__(self): return self.name
    def get_absolute_url(self): return reverse('home')

class Order(models.Model):
    STATUS_CHOICES = [('pending','Pending'),('paid','Paid')]
    order_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    shipping_address = models.TextField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='paid')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.order_number

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)
    price_at_order = models.DecimalField(max_digits=10, decimal_places=2)

# Create your models here.
