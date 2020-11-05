from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Orderdetail)
admin.site.register(Cart)
admin.site.register(Cart_Product)
admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Category_Product)