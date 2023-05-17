from django.shortcuts import render, get_object_or_404, redirect

from accounts.forms import OrderForm
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


def customer_view(request,pk):
    customer= Customer.objects.get(id=pk)
    orders=customer.order_set.all()
    context={'customer':customer, 'orders':orders}
    return render(request, 'accounts/customer.html',context)

def create_order_form(request):
    form=OrderForm()
    if request.method=='POST':
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account/dashboard')
    context={'form':form}
    return render(request,'accounts/order_form.html',context)


def update_order_form(request,pk):
    order=Order.objects.get(id=pk)
    form=OrderForm(instance=order)
    if request.method=='POST':
        form=OrderForm(request.POST,instance=order)
        form.save()
        return redirect('/account/dashboard/')
    context={'order':order,'form':form}
    return render(request,'accounts/order_form.html',context)

def delete_order_form(request,pk):
    order=Order.objects.get(id=pk)
    if request.method=='POST':
        order.delete()
        return redirect('/account/dashboard/')
    context={'item':order}
    return render(request,'accounts/delete_order.html',context)
