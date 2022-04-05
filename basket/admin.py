from django.contrib import admin
import basket.models

admin.site.register(basket.models.Order)
admin.site.register(basket.models.OrderItem)

