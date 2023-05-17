from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('customer/<str:pk>/', views.customer_view,name='customer'),
    path('products/', views.products_view,name='product'),

    #crud
    path('create-order/',views.create_order_form,name='create_order'),
    path('update-order/<str:pk>/',views.update_order_form, name='update_order'),
    path('delete-order/<str:pk>/',views.delete_order_form, name='delete_order')
]
