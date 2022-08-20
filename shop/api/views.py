from rest_framework import mixins, generics

from shop.api.serializers import ProductSerializer
from shop.models import Product


class ProductViewSet(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get(self, request, pk=None):
        if not pk:
            return self.list(request)
        return self.retrieve(request, pk)

