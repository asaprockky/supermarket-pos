from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class HomeView(TemplateView):
    template_name = 'market/main.html'


class AdminPanelView(TemplateView):
    template_name = 'market/admin_dashboard.html'


class AdminProductsView(TemplateView):
    template_name = 'market/admin_products.html'

class AdminInventory(TemplateView):
    template_name = 'market/admin_inventory.html'

class AdminSales(TemplateView):
    template_name = 'market/admin_sales.html'