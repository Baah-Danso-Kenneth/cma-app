from django.shortcuts import render, get_object_or_404
from accounts.models import Product, Customer, Order


def dashboard(request):
    customers=Customer.objects.all()
    products=Product.objects.all()
    orders=Order.objects.all()

    total_orders=orders.count()
    orders_delivered=orders.filter(status='DELIVERED').count()
    orders_pending=orders.filter(status='PENDING').count()

    context={'customers':customers,
             'products':products,
             'orders':orders,
             'total_orders':total_orders,
             'orders_delivered':orders_delivered,
             'orders_pending':orders_pending}

    return render(request, 'accounts/dashboard.html',context)


def products_view(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products': products})


def customer_view(request,id=None):
    customer= get_object_or_404(Customer,id=id)
    orders=Order.objects.all()
    return render(request, 'accounts/customer.html',{'customer':customer,'orders':orders})
