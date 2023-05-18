from django.urls import path
from . import views
app_name='student'

urlpatterns = [
    path ('customer_home/',views.get_customer_home, name="customer_home"),
    path ('customer_master/',views.get_customer_master, name="customer_master")
    
]