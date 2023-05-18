from django.contrib import admin
from .models import Customer, Order, Product, Tags


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name','phone','id']
    list_filter = ['name','phone','date_created']
    search_fields = ['name']

admin.site.register(Order)
admin.site.register(Tags)
admin.site.register(Product)