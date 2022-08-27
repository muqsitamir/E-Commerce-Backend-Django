from django.db import models
from django.db.models import signals
from django.dispatch import receiver


class Product(models.Model):
    title = models.CharField(max_length=50)
    price = models.FloatField()
    shipping = models.BooleanField(default=True)
    description = models.TextField()
    sale_price = models.FloatField()
    image = models.ImageField(null=True)

    def __str__(self):
        return self.title


@receiver(signals.post_delete, sender=Product)
def delete_image(sender, instance, **kwargs):
    instance.image.delete()
