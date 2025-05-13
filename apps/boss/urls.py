from django.urls import path
from . import views


urlpatterns = [
    path('', views.BossMainView.as_view(), name= 'boss_dashboard'),
    path('boss-market-details/', views.BossMarketDetails.as_view(), name= 'boss_market_details'),
    path('boss-users/', views.BossUsers.as_view(), name= 'boss_users'),
    path('boss-signup/', views.SignUpVIew.as_view(), name= 'boss_signup'),
    path('boss-login/', views.BossLoginView.as_view(), name= 'boss-login')
]