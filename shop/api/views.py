import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from shop.models import Product


@csrf_exempt
def product_view(request, product_id=None):
    if request.method == 'GET':
        if product_id:
            product = Product.objects.filter(id=product_id).values()
            if product.exists():
                return HttpResponse(json.dumps(product[0], indent=4), status=200)
            else:
                return HttpResponse(json.dumps({'error': "Not Found"}, indent=4), status=200)
        page, limit = int(request.GET.get('page', '0')), request.GET.get('limit', 12)
        products = [product for product in Product.objects.all()[page*limit:page*limit+limit].values()]
        return HttpResponse(json.dumps(products, indent=4), status=200)
    elif request.method == "POST":
        product = Product.objects.create(**json.loads(request.body))
        product.save()
        return HttpResponse(json.dumps(Product.objects.filter(id=product.id).values()[0], indent=4), status=201)
    elif request.method == "PUT":
        try:
            product = Product.objects.get(id=product_id)
            body = json.loads(request.body)
            for k, v in body.items():
                setattr(product, k, v)
            product.save()
            product = Product.objects.filter(id=product_id).values()
            return HttpResponse(json.dumps(product[0], indent=4), status=200)
        except Exception as E:
            pass
    elif request.method == "DELETE":
        try:
            product = Product.objects.get(id=product_id)
            product.delete()
            return HttpResponse(status=204)

        except Exception as E:
            pass
