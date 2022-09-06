from django.db import models
from django.db.models import signals
from django.dispatch import receiver


class Sport(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(null=True, blank=True)
    description = models.CharField(max_length=100, null=True)
    nav_image1 = models.ImageField(null=True, blank=True)
    nav_image2 = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


@receiver(signals.post_delete, sender=Sport)
def delete_image(sender, instance, **kwargs):
    instance.image.delete()


class Category(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(null=True, blank=True)
    sport = models.ForeignKey(Sport, null=False, related_name="categories", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


@receiver(signals.post_delete, sender=Category)
def delete_image(sender, instance, **kwargs):
    instance.image.delete()


class SubCategory(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(null=True, blank=True)
    category = models.ForeignKey(Category, null=False, related_name="sub_categories", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


def get_sub_category():
    return SubCategory.objects.get(id=1)


@receiver(signals.post_delete, sender=SubCategory)
def delete_image(sender, instance, **kwargs):
    instance.image.delete()


class Product(models.Model):
    title = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)
    subcategory = models.ForeignKey(SubCategory, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


@receiver(signals.post_delete, sender=Product)
def delete_image(sender, instance, **kwargs):
    instance.image.delete()


class Message(models.Model):
    message = models.CharField(max_length=100)
    link = models.CharField(max_length=200, default=None, null=True, blank=True)

    def __str__(self):
        return self.message
