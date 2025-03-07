from django.urls import path
from .views import signup, custom_login, farmer_dashboard, buyer_dashboard, homepage, generate_contract, list_crops

urlpatterns = [
    path('', homepage, name='homepage'),  
    path('signup/', signup, name='signup'),
    path('login/', custom_login, name='login'),
    path("farmer/dashboard/", farmer_dashboard, name="farmer_dashboard"),
    path("buyer/dashboard/", buyer_dashboard, name="buyer_dashboard"),
    path('contract/', generate_contract, name='generate_contract'),
    path('list-crops/', list_crops, name='list_crops')
]
