from django.db import models
from django.contrib.auth.models import User

# Create your models here.

from django.db import models
import uuid
ROLE_CHOICES = [
    ('owner', 'Owner'),
    ('cashier', 'Cashier'),
]


class Market(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, verbose_name="Do'kon Nomi")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='markets', verbose_name="Egasi")
    address = models.TextField(blank=True, verbose_name="Manzil")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan Sana")

    class Meta:
        verbose_name = "Do'kon"
        verbose_name_plural = "Do'konlar"

    def __str__(self):
        return self.name
class Notification(models.Model):
    id = models.AutoField(primary_key= True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null= True)
    market = models.ForeignKey('Market', null= True, blank= True, on_delete= models.CASCADE)
    message = models.CharField(max_length= 124)
    is_read = models.BooleanField(default= False)
    created_at = models.DateTimeField(auto_now_add= True)

PAYMENT_METHOD_CHOICES = [
    ('cash', 'Cash'),
    ('card', 'Card'),
    ('transfer', 'Bank Transfer'),
    ('other', 'Other'),
]


class Product(models.Model):
    id = models.IntegerField(primary_key= True)
    product_name = models.CharField(max_length= 128)
    stock = models.PositiveIntegerField(default= 0)
    barcode = models.CharField(max_length= 128, unique= True, blank= True)
    price = models.DecimalField(max_digits= 20, decimal_places= 2)
    cost = models.DecimalField(max_digits= 20, decimal_places= 2)
    description = models.TextField(blank=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)
    market = models.ForeignKey(Market, on_delete=models.CASCADE)
    pr_created_at = models.DateTimeField(auto_now_add=True)
    pr_updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.product_name} - {self.market.name}"
    

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    market = models.ForeignKey(Market, on_delete= models.CASCADE)
    transaction_created_at = models.DateTimeField(auto_now_add= True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    payment_method = models.CharField(max_length= 20, choices= PAYMENT_METHOD_CHOICES)

    def __str__(self):
        return f"#{self.id} - {self.user.telegram} - {self.payment_method}"

class TransactionItem(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)

    def get_total_price(self):
        return self.quantity * self.price_per_unit

    def __str__(self):
        return f"{self.quantity} x {self.product_name}"
    




