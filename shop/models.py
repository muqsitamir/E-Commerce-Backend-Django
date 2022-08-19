from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=50)
    price = models.FloatField()
    shipping = models.BooleanField(default=True)
    description = models.TextField()
    sale_price = models.FloatField()
    image = models.ImageField(default='https://storage.googleapis.com/proudcity/mebanenc/uploads/2021/03/placeholder-image-300x225.png')

    def __str__(self):
        return self.title
