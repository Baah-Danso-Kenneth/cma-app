from django.urls import path
from . import views
from django.contrib.auth import views as auth_view


app_name = 'accounts'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('customer/<str:pk>/', views.customer_view,name='customer'),
    path('products/', views.products_view,name='product'),

    #crud
    path('create-order/',views.create_order_form,name='create_order'),
    path('update-order/<str:pk>/',views.update_order_form, name='update_order'),
    path('delete-order/<str:pk>/',views.delete_order_form, name='delete_order'),

    #password-reset,
    path('reset_password/',auth_view.PasswordResetView.as_view(),name='reset_password'),
    path('reset_password_sent/', auth_view.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uid64>/<token>/', auth_view.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset_password/',auth_view.PasswordResetConfirmView.as_view,name='password_reset_complete'),
    
    #authentication
    path('register/users',views.registerUser, name='register'),
    path('login/users',views.loginUser, name='login'),
    path('logout/users', views.logoutUser, name='logout'),

    path('user/view',views.user_view, name='user_view'),

]
