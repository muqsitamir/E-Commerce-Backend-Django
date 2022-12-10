from rest_framework.viewsets import ModelViewSet

from shop.api.serializers import CategorySerializer, ProductSerializer, MessageSerializer, FeaturedImageSerializer
from shop.models import Product, Message, Category, FeaturedImage


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(parent=None).all()

    def get_queryset(self):
        category_id = self.request.query_params.get('id', None)
        if category_id is not None:
            self.queryset = Category.objects.filter(id=category_id)
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
