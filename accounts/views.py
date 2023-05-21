from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from accounts.decorators import unauthenticated_user, allowed_users, admin_only
from accounts.forms import OrderForm, CreateUserForm, LoginUserForm, CustomerForm
from accounts.models import Product, Customer, Order
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url='/account/login/users')
@admin_only
def dashboard(request):
    customers = Customer.objects.all()
    products = Product.objects.all()
    orders = Order.objects.all()

    total_orders = orders.count()
    orders_delivered = orders.filter(status='DELIVERED').count()
    orders_pending = orders.filter(status='PENDING').count()

    context = {'customers': customers,
               'products': products,
               'orders': orders,
               'total_orders': total_orders,
               'orders_delivered': orders_delivered,
               'orders_pending': orders_pending}

    return render(request, 'accounts/dashboard.html', context)


@login_required(login_url='/account/login/users')
@allowed_users(allowed_roles=['admin'])
def products_view(request):
    products_list = Product.objects.all()

    paginator = Paginator(products_list, 5)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    except EmptyPage:
        posts = paginator.page(page_number.numb_pages)
    except PageNotAnInteger:
        paginator.page(1)
    return render(request, 'accounts/products.html', {'posts': posts})


@login_required(login_url='/account/login/users')
@allowed_users(allowed_roles=['admin'])
def customer_view(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    context = {'customer': customer, 'orders': orders}
    return render(request, 'accounts/customer.html', context)


@login_required(login_url='/account/login/users')
@allowed_users(allowed_roles=['admin'])
def create_order_form(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account/dashboard')
    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)


@login_required(login_url='/account/login/users')
@allowed_users(allowed_roles=['admin'])
def update_order_form(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        form.save()
        return redirect('/account/dashboard/')
    context = {'order': order, 'form': form}
    return render(request, 'accounts/order_form.html', context)


@login_required(login_url='/account/login/users')
@allowed_users(allowed_roles=['admin'])
def delete_order_form(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/account/dashboard/')
    context = {'item': order}
    return render(request, 'accounts/delete_order.html', context)


@unauthenticated_user
def registerUser(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Successfully created' + username)

            return redirect('/account/login/users')
    form = CreateUserForm()
    context = {'form': form}
    return render(request, 'accounts/register.html', context)


@unauthenticated_user
def loginUser(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])

            if user is not None:
                login(request, user)
                return redirect('/account/dashboard/')
            else:
                messages.info(request, 'Username and password incorrect')
    else:
        form = LoginUserForm()
    context = {'form': form}
    return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('/account/login/users')


@login_required(login_url='/account/login/users')
@allowed_users(allowed_roles=['customer'])
def user_view(request):
    order = request.user.customer.order_set.all()
    print(order)
    total_orders = order.count()
    orders_pending = order.filter(status='PENDING').count()
    orders_delivered = order.filter(status='DELIVERED').count()

    context = {'order': order,
               'total_orders': total_orders,
               'orders_delivered': orders_delivered,
               'orders_pending': orders_pending
               }

    return render(request, 'accounts/user_page.html', context)


@login_required(login_url='/account/login/users')
@allowed_users(allowed_roles=['customer'])
def account_setting(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)

    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'accounts/account_setting.html', context)
