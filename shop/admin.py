from django.contrib import admin

from shop.models import Product, Message, Category, SubCategory, Sport


class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "description",)
    search_fields = ("title",)


class SportAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "sport")
    search_fields = ("name",)


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "category",)
    search_fields = ("name", "category__name",)


class MessageAdmin(admin.ModelAdmin):
    list_display = ("message", "link",)
    search_fields = ("message",)


admin.site.register(Product, ProductAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Sport, SportAdmin)
