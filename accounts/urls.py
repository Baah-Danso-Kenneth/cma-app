from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    # authentication
    path('register/users', views.registerUser, name='register'),
    path('login/users', views.loginUser, name='login'),
    path('logout/users', views.logoutUser, name='logout'),

    # password-reset
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name='password_reset'),
    path('password-reset-done/',auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_solid.html'),name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm_form.html'),name='password_reset_confirm'),
    path('password-reset-complete-done/',auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_confirm_done.html'),name='password_reset_complete'),

    #pages
    path('dashboard/', views.dashboard, name='dashboard'),
    path('customer/<str:pk>/', views.customer_view,name='customer'),
    path('products/', views.products_view,name='product'),
    path('setting/',views.account_setting,name='setting'),

    #crud
    path('create-order/',views.create_order_form,name='create_order'),
    path('update-order/<str:pk>/',views.update_order_form, name='update_order'),
    path('delete-order/<str:pk>/',views.delete_order_form, name='delete_order'),



    path('user/view',views.user_view, name='user_view'),

]
