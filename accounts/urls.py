from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('customer/',views.customer_view,name='customer'),
    path('products/',views.products_view,name='product')
]
