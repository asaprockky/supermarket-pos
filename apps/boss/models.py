from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser
ROLE_CHOICES = [
    ('owner', 'Owner'),
    ('cashier', 'Cashier'),
]

class UserProfile(AbstractUser):  # ✅ Inherit from models.Model
    telegram = models.CharField(unique=True, max_length=30)
    password = models.CharField(max_length=128)  # Hashed manually or by auth system
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='cashier')
    market = models.ForeignKey('Market', null=True, blank=True, on_delete=models.SET_NULL)
    balance = models.IntegerField(null= True, blank= True)
    last_payment = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'telegram'    
    REQUIRED_FIELDS = ['first_name', 'last_name']   
    def __str__(self):
        return f"{self.user.username}'s Profile"

class Market(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, verbose_name="Do'kon Nomi")
    owner = models.ForeignKey('UserProfile', on_delete=models.CASCADE, related_name='markets', verbose_name="Egasi")
    address = models.TextField(blank=True, verbose_name="Manzil")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan Sana")

    class Meta:
        verbose_name = "Do'kon"
        verbose_name_plural = "Do'konlar"

    def __str__(self):
        return self.name
class Notification(models.Model):
    id = models.AutoField(primary_key= True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null= True)
    market = models.ForeignKey('Market', null= True, blank= True, on_delete= models.CASCADE)
    message = models.CharField(max_length= 124)
    is_read = models.BooleanField(default= False)
    created_at = models.DateTimeField(auto_now_add= True)
