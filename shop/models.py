from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=50)
    price = models.FloatField()
    shipping = models.BooleanField(default=True)
    description = models.TextField()
    sale_price = models.FloatField()
    # image = models.ImageField()

    def __str__(self):
        return self.title
