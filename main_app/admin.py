from django.contrib import admin

# Register your models here.
from .models import Chocolate, Order

admin.site.register(Chocolate)
admin.site.register(Order)