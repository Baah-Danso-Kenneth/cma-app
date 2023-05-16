from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('customer/',views.customer,name='customer'),
    path('products/',views.products,name='product')
]
