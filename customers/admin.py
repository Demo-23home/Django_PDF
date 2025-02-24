from django.contrib import admin
from .models import Customer


# @admin.register(Customer)
# class ModelCustomer(admin.ModelAdmin): 
#     list_display = "__all__"

admin.site.register(Customer)