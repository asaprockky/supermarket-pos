from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name= 'home_market'),
    path('admin_panel/', views.AdminPanelView.as_view(), name= 'admin_panel'),
    path('admin_products/', views.AdminProductsView.as_view(), name= 'admin_products'),
    path('admin_inventory/', views.AdminInventory.as_view(), name= 'admin_inventory'),
    path('admin_sales/', views.AdminSales.as_view(), name= 'admin_sales')
]