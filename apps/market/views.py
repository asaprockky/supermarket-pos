from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib import messages
from .models import Product, Market, Transaction, TransactionItem
from .forms import MarketLoginForm, AddProductFOrm
from django.contrib.auth import login
from django.views import View
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.edit import FormView
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.dateparse import parse_date
import json
# Create your views here.



class AdminLoginView (LoginView):
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
    def post(self, request):
        cart_raw = request.POST.get("cart_json", "[]")
        payment_amount = request.POST.get("payment_amount")

        try:
            cart = json.loads(cart_raw)
            print("DECODED CART:", cart)
            print(payment_amount)

            market = get_object_or_404(Market, owner=request.user)

            total_amount = 0
            for item in cart:
                total_amount += item.get("unit_price", 0) * item.get("qty", 0)

            # ✅ First create Transaction
            transaction = Transaction.objects.create(
                total_price=total_amount,
                payment_method="cash",
                market=market,
                user=request.user
            )

            # ✅ Then create related TransactionItems
            for item in cart:
                TransactionItem.objects.create(
                    transaction=transaction,
                    product_id=item.get("product_id"),  
                    quantity=item.get("qty"),
                    price_per_unit=item.get("unit_price")
                )
                product = get_object_or_404(Product, id=item.get("product_id"))
                quantity = item.get("qty")
                product.stock -= quantity
                product.save()

        except json.JSONDecodeError as e:
            print("JSON ERROR:", e)
            messages.error(request, "Cart ma'lumotini o'qib bo'lmadi.")
            return redirect("home_market")

        messages.success(request, "Raxmat! To'lov muvaffaqiyatli amalga oshirildi.")
        return redirect('home_market')



class AdminPanelView(LoginRequiredMixin, TemplateView):
    template_name = 'market/admin_dashboard.html'


class AdminProductsView(LoginRequiredMixin, FormView):
    model = Product
    template_name = 'market/admin_products.html'
    form_class = AddProductFOrm
    success_url = reverse_lazy("admin_products")
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # all products that belong to any market owned by this user
        products = Product.objects.filter(market__owner=self.request.user)
        context["products"] = products
        return context
    def form_valid(self, form):
        # attach the market automatically
        market = get_object_or_404(Market, owner=self.request.user)
        product = form.save(commit=False)
        product.market = market
        product.save()
        messages.success(self.request, "Maxsulot Qo'shildi")
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request, "Maxsulot Qo'shishda Xatolik!")
        ctx = self.get_context_data(form=form)
        ctx["show_add_modal"] = True
        return self.render_to_response(ctx)


def delete_product(request, pk):
    if request.method == "POST":
        product = get_object_or_404(Product, pk= pk, market__owner=request.user )
        product.delete()
        messages.success(request, "Product deleted.")
    return redirect("admin_products")

def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk, market__owner=request.user)
    if request.method == "POST":
        form = AddProductFOrm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Product updated.")
        else:
            print("form errors:", form.errors)          # console
            messages.error(request, form.errors) 
    return redirect("admin_products")


class UpdateRestockLevel(LoginRequiredMixin, View):
    def post(self, request, pk):
        market  = get_object_or_404(Market, owner=request.user)
        product = get_object_or_404(Product, pk=pk, market=market)

        try:
            new_level = int(request.POST.get("restock_level"))
            if new_level <= 0:
                raise ValueError
        except (TypeError, ValueError):
            messages.error(request, "Restock darajasi musbat son bo‘lishi kerak.")
            return redirect("admin_inventory")

        product.restock_level = new_level
        product.save(update_fields=["restock_level"])
        messages.success(request, f"«{product.product_name}» restock darajasi {new_level} ga o‘zgartirildi.")
        return redirect("admin_inventory")
    
class RestockProduct(LoginRequiredMixin, View):
    def post(self, request, pk):
        market  = get_object_or_404(Market, owner=request.user)
        product = get_object_or_404(Product, pk=pk, market=market)

        try:
            qty = int(request.POST.get("quantity"))
            if qty <= 0:
                raise ValueError
        except (TypeError, ValueError):
            messages.error(request, "Miqdor musbat son bo‘lishi kerak.")
            return redirect("admin_inventory")

        product.stock += qty
        product.save(update_fields=["stock"])
        messages.success(request, f"{product.product_name} +{qty} ta qo‘shildi (yangi qoldiq: {product.stock}).")
        return redirect("admin_inventory")
class AdminInventory(LoginRequiredMixin, TemplateView):
    model = Product
    template_name = 'market/admin_inventory.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.objects.filter(market__owner=self.request.user)
        context["products"] = products
        return context
class AdminSales(LoginRequiredMixin, TemplateView):
    template_name = "market/admin_sales.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # grab query-string params ?start=YYYY-MM-DD&end=YYYY-MM-DD
        start_raw = self.request.GET.get("start")
        end_raw   = self.request.GET.get("end")

        # safely convert to date objects (returns None if blank)
        start = parse_date(start_raw) if start_raw else None
        end   = parse_date(end_raw) if end_raw else None

        market = Market.objects.filter(owner=self.request.user).first()

        qs = Transaction.objects.filter(market=market)
        if start:
            qs = qs.filter(transaction_created_at__date__gte=start)
        if end:
            qs = qs.filter(transaction_created_at__date__lte=end)

        context["transactions"] = qs
        context["start"] = start_raw
        context["end"] = end_raw
        return context
        


    