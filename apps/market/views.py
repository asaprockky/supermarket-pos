from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from .models import Product
from .forms import MarketLoginForm
from django.contrib.auth import login
from django.views import View
from django.http import JsonResponse
from django.template.loader import render_to_string
# Create your views here.


class AdminLoginVIew(LoginView):
    form_clas = MarketLoginForm
    template_name = 'market/login.html'
    redirect_authenticated_user = True

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, form.get_user())
        return super().form_valid(form)
    
class ProductAutocomplete(View):
    def get(self, request):
        q = request.GET.get('q', '')
        products = Product.objects.filter(product_name__icontains=q)[:8]
        html = render_to_string('market/_product_list.html', {'products': products})
        return JsonResponse({'html': html})
    
    
class HomeView(LoginRequiredMixin, ListView):
    template_name = 'market/main.html'
    model  = Product
    def get_queryset(self):
        self.search_query = self.request.GET.get('q', '')
        if self.search_query:
            data = Product.objects.filter(product_name__icontains = self.search_query)
            print(data)
            return data
        else:
            print("No Product found")
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user
        full_name = f"{user.first_name} {user.last_name}".strip()
        context['first_name'] = full_name or user.username
        context['search_query'] = self.search_query  # Now this works fine
        return context


class AdminPanelView(LoginRequiredMixin, TemplateView):
    template_name = 'market/admin_dashboard.html'


class AdminProductsView(LoginRequiredMixin, TemplateView):
    # products = Market.objects.filter(market = "")
    template_name = 'market/admin_products.html'

class AdminInventory(LoginRequiredMixin, TemplateView):
    template_name = 'market/admin_inventory.html'

class AdminSales(LoginRequiredMixin, TemplateView):
    template_name = 'market/admin_sales.html'