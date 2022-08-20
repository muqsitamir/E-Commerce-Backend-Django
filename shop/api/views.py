import json

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status

from shop.api.serializers import ProductSerializer
from shop.models import Product


@csrf_exempt
def product_view(request, product_id=None):
    if request.method == 'GET':
        if product_id:
            try:
                return JsonResponse(ProductSerializer(Product.objects.get(id=product_id)).data, status=status.HTTP_200_OK)
            except Product.DoesNotExist:
                return JsonResponse({'error': "Not Found"}, status=status.HTTP_404_NOT_FOUND)
        page, limit = int(request.GET.get('page', '0')), request.GET.get('limit', 12)
        return JsonResponse(ProductSerializer(Product.objects.all()[page*limit:page*limit+limit], many=True).data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        product_s = ProductSerializer(data=json.loads(request.body))
        if product_s.is_valid():
            product_s.save()
            return JsonResponse(product_s.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(product_s.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "PATCH":
        try:
            product_s = ProductSerializer(Product.objects.get(id=product_id), data=json.loads(request.body))
            if product_s.is_valid():
                product_s.save()
                return JsonResponse(product_s.data, status=status.HTTP_201_CREATED)
            else:
                return JsonResponse(product_s.errors, status=status.HTTP_400_BAD_REQUEST)
        except Product.DoesNotExist as E:
            return JsonResponse({'error': "Not Found"}, status=status.HTTP_404_NOT_FOUND)
    elif request.method == "DELETE":
        try:
            product = Product.objects.get(id=product_id)
            product.delete()
            return HttpResponse(status=204)
        except Product.DoesNotExist:
            return JsonResponse({'error': "Not Found"}, status=status.HTTP_404_NOT_FOUND)
