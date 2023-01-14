from rest_framework import serializers

from shop.models import Product, Message, Category, FeaturedImage


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'parent', 'children', 'description', 'nav_image1', 'nav_image2', "image",)

    def get_fields(self):
        fields = super(CategorySerializer, self).get_fields()
        fields['children'] = CategorySerializer(many=True)
        return fields


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"


class FeaturedImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeaturedImage
        fields = "__all__"
