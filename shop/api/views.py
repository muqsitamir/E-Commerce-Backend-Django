from rest_framework.viewsets import ModelViewSet

from shop.api.serializers import CategorySerializer, ProductSerializer, MessageSerializer, FeaturedImageSerializer
from shop.models import Product, Message, Category, FeaturedImage


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(parent=None).all()

    def get_queryset(self):
        category_name = self.request.query_params.get('category_name', None)
        if category_name is not None:
            self.queryset = Category.objects.filter(name=category_name.split(",")[-1])
            if len(category_name.split(",")) > 1:
                parents = category_name.split(',')[0:-1][::-1]
                keyword = "parent__"
                query = {}
                for category in parents:
                    query[keyword + "name"] = category
                    keyword = keyword + keyword
                self.queryset = self.queryset.filter(**query)
        return self.queryset


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class MessageViewSet(ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()


class FeaturedImageViewSet(ModelViewSet):
    serializer_class = FeaturedImageSerializer
    queryset = FeaturedImage.objects.all()

    def get_queryset(self):
        category_name = self.request.query_params.get('category_name', None)
        if category_name is not None:
            self.queryset = FeaturedImage.objects.filter(category__name=category_name)
        return self.queryset
