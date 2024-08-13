from django.contrib import admin
from .models import samples, natural_products, car_spare_part, orders

class sampledmin(admin.ModelAdmin):
    list_display = ['item_title', 'item_disc']

class ordersadmin(admin.ModelAdmin):
    list_display = ['user_name', 'orderd_item']

admin.site.register(samples, sampledmin)
admin.site.register(natural_products, sampledmin)
admin.site.register(car_spare_part, sampledmin) 
admin.site.register(orders, ordersadmin) 

