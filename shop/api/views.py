from rest_framework import mixins, generics

from shop.api.serializers import ProductSerializer
from shop.models import Product


class ProductViewSet(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get_queryset(self):
        page, limit = int(self.request.GET.get('page', '0')), self.request.GET.get('limit', 12)
        return Product.objects.all()

    def get(self, request, pk=None):
        if not pk:
            return self.list(request)
        return self.retrieve(request, pk)

    def post(self, request):
        return self.create(request)

    def patch(self, request, pk):
        return self.update(request, pk,partial=True)

    def delete(self, request, pk):
        return self.destroy(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)


