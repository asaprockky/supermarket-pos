from django.contrib import admin
from .models import Product, Category, Market
# Register your models here.
@admin.register(Market)
class MarketAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'created_at')
    search_fields = ('name', 'owner__username')
    list_filter = ('owner',)

    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display   = ('id', 'product_name', 'stock', 'price', 'market', 'category')
    list_filter    = ('market', 'category')       
    search_fields  = ('product_name', 'barcode')  
    ordering       = ('-pr_created_at',)

    readonly_fields = ('pr_created_at', 'pr_updated_at')
    fieldsets = (
        ('Basic info', {
            'fields': ('product_name', 'barcode', 'category', 'market'),
        }),
        ('Inventory & pricing', {
            'fields': (('stock', 'price', 'cost'),),
        }),
        ('Timestamps', {
            'classes': ('collapse',),
            'fields': (('pr_created_at', 'pr_updated_at'),),
        }),
    )