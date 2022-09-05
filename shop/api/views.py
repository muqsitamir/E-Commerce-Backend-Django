from rest_framework.viewsets import ModelViewSet, generics


from shop.api.serializers import MessageSerializer, SportNavSerializer
from shop.models import Product, Message, Sport


class SportViewSet(ModelViewSet):
    serializer_class = SportNavSerializer
    queryset = Sport.objects.all()

    def get_queryset(self):
        queryset = Sport.objects.all()
        sport_id = self.request.query_params.get('sport_id', None)
        if sport_id is not None:
            queryset = queryset.filter(id=sport_id)
        return queryset

#
# class ProductViewSet(ModelViewSet):
#     serializer_class = ProductSerializer
#     queryset = Product.objects.all()


class MessageViewSet(ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
