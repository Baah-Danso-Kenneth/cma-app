from django.contrib import admin
from .models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name','phone','id']
    list_filter = ['name','phone','date_created']
    search_fields = ['name']