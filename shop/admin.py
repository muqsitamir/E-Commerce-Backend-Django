from django.contrib import admin

from shop.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "price", 'shipping', "sale_price", "description", 'image')
    list_filter = ("shipping",)
    search_fields = ("title",)

admin.site.register(Product, ProductAdmin)
