from django.contrib import admin
import core.models

admin.site.register(core.models.Category)
admin.site.register(core.models.Product)
admin.site.register(core.models.Pharmacy)
admin.site.register(core.models.Available)
admin.site.register(core.models.Cart)
admin.site.register(core.models.CartItem)
