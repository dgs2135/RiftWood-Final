from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings

class Testimonial(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user.username} - {self.created_at}"

class ContactQuery(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class PageContent(models.Model):
    page_name = models.CharField(max_length=50, unique=True)
    content = models.TextField()
    def __str__(self):
        return self.page_name

class CustomOrder(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('in_production', 'In Production'),
        ('quality_check', 'Quality Check'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]

    CATEGORY_CHOICES = [
        ('electric_guitar', 'Custom Electric Guitar'),
        ('bass', 'Custom Bass Guitar'),
        ('drums', 'Custom Drum Kit'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    instrument = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    specifications = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)