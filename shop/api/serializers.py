from rest_framework import serializers

from shop.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

    # def create(self, validated_data):
        # return super().create(validated_data)
# from shop.models import *
# from shop.api.serializers import *
# body = {
#     "title": "updated again",
#     "price": 10.0,
#     "shipping": False,
#     "description": "kmskasmk",
#     "sale_price": 11000.0,
# }
# p = ProductSerializer(data=body)