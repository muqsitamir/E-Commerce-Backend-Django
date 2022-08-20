import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from shop.api.serializers import ProductSerializer
from shop.models import Product


class ProductAPIView(APIView):
    permission_classes = [AllowAny]

    def get_object(self, pk):
        try:
            return Product.objects.get(id=pk)
        except Product.DoesNotExist:
            return Response({'error': "Not Found"}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, product_id):
        if product_id:
            product = self.get_object(product_id)
            if not isinstance(product, Product):
                return product
            serializer = ProductSerializer(product)
        else:
            page, limit = int(request.GET.get('page', '0')), request.GET.get('limit', 12)
            products = Product.objects.all()[page * limit:page * limit + limit]
            serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, product_id):
        product = self.get_object(product_id)
        if not isinstance(product, Product):
            return product
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, product_id):
        product = self.get_object(product_id)
        if not isinstance(product, Product):
            return product
        product.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)





@csrf_exempt
def product_view(request, product_id=None):
    if request.method == 'GET':
        if product_id:
            try:
                return Response(ProductSerializer(Product.objects.get(id=product_id)).data, status=status.HTTP_200_OK)
            except Product.DoesNotExist:
                return Response({'error': "Not Found"}, status=status.HTTP_404_NOT_FOUND)
        page, limit = int(request.GET.get('page', '0')), request.GET.get('limit', 12)
        return Response(ProductSerializer(Product.objects.all()[page*limit:page*limit+limit], many=True).data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        product_s = ProductSerializer(data=json.loads(request.body))
        if product_s.is_valid():
            product_s.save()
            return Response(product_s.data, status=status.HTTP_201_CREATED)
        else:
            return Response(product_s.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "PATCH":
        try:
            product_s = ProductSerializer(Product.objects.get(id=product_id), data=json.loads(request.body))
            if product_s.is_valid():
                product_s.save()
                return Response(product_s.data, status=status.HTTP_201_CREATED)
            else:
                return Response(product_s.errors, status=status.HTTP_400_BAD_REQUEST)
        except Product.DoesNotExist as E:
            return Response({'error': "Not Found"}, status=status.HTTP_404_NOT_FOUND)
    elif request.method == "DELETE":
        try:
            product = Product.objects.get(id=product_id)
            product.delete()
            return HttpResponse(status=204)
        except Product.DoesNotExist:
            return Response({'error': "Not Found"}, status=status.HTTP_404_NOT_FOUND)
