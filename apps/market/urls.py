from django.urls import path
from . import views
from .views import UpdateRestockLevel, RestockProduct
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.HomeView.as_view(), name= 'home_market'),
    path('admin_panel/', views.AdminPanelView.as_view(), name= 'admin_panel'),
    path('admin_products/', views.AdminProductsView.as_view(), name= 'admin_products'),
    path('admin_inventory/', views.AdminInventory.as_view(), name= 'admin_inventory'),
    path('admin_sales/', views.AdminSales.as_view(), name= 'admin_sales'),
    path('admin_login/', views.AdminLoginView.as_view(), name= 'login'),
    path('admin_signup/', views.AdminLoginView.as_view(), name= 'admin_signup'),
    path('api/products/', views.ProductAutocomplete.as_view(), name='product-autocomplete'),
    path('admin_products/<int:pk>/delete/', views.delete_product, name='delete_product'),
    path('admin_products/<int:pk>/edit_product/', views.edit_product, name='edit_product'),
    path("product/<int:pk>/restock-level/", UpdateRestockLevel.as_view(), name="update_restock_level"),
    path("product/<int:pk>/restock/",RestockProduct.as_view(),     name="restock_product"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout")

]