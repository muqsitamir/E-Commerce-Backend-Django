from django.contrib import admin

from shop.models import Product, Message, Category, FeaturedImage


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "parent",)
    search_fields = ["id", "name", "description", "parent__name"]
    ordering = ("id",)


class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "price")
    search_fields = ("title", "category")


class MessageAdmin(admin.ModelAdmin):
    list_display = ("message", "link",)
    search_fields = ("message",)


class FeaturedImageAdmin(admin.ModelAdmin):
    list_display = ("name", "link", 'category')
    search_fields = ("name",)


admin.site.register(Product, ProductAdmin)
admin.site.register(FeaturedImage, FeaturedImageAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Category, CategoryAdmin)

