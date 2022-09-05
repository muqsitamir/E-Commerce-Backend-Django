from rest_framework import serializers

from shop.models import Product, Message, Category, Sport, SubCategory

#
# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = "__all__"
#


class SubCategoryNavSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ("name",)


class CategoryNavSerializer(serializers.ModelSerializer):
    sub_categories = SubCategoryNavSerializer(many=True)

    class Meta:
        model = Category
        fields = ("name", "sub_categories")


class SportNavSerializer(serializers.ModelSerializer):
    categories = CategoryNavSerializer(many=True)

    class Meta:
        model = Sport
        fields = ('name', 'description', 'categories')


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"
