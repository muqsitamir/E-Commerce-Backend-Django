from rest_framework.viewsets import ModelViewSet

from shop.api.serializers import ProductSerializer
from shop.models import Product


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
