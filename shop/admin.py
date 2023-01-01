from django.contrib import admin

from shop.models import Product, Message, Category, FeaturedImage, Color, Image


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "parent",)
    search_fields = ["id", "name", "description", "parent__name"]
    ordering = ("id",)


class ProductAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)


class ColorAdmin(admin.ModelAdmin):
    list_display = ("name", "color",)
    search_fields = ("name",)


class MessageAdmin(admin.ModelAdmin):
    list_display = ("message", "link",)
    search_fields = ("message",)


class FeaturedImageAdmin(admin.ModelAdmin):
    list_display = ("name", "link", 'category')
    search_fields = ("name",)


class ImageAdmin(admin.ModelAdmin):
    list_display = ("product", "color",)
    search_fields = ("product", "color", )


admin.site.register(Product, ProductAdmin)
admin.site.register(FeaturedImage, FeaturedImageAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(Image, ImageAdmin)

