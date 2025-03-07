from django.contrib import admin
from django.urls import path
from users import views  

urlpatterns = [
    path("", views.homepage, name="homepage"),  
    path("admin/", admin.site.urls),
    path("signup/", views.signup, name="signup"),
    path("login/", views.custom_login, name="login"),
    path("farmer/dashboard/", views.farmer_dashboard, name="farmer_dashboard"),
    path("buyer/dashboard/", views.buyer_dashboard, name="buyer_dashboard"),
    path("contract/", views.generate_contract, name="generate_contract"),
    path('list-crops/', views.list_crops, name="list_crops")
]
