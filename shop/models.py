from django.db import models
from colorfield.fields import ColorField
from django.db.models import signals
from django.dispatch import receiver


class Category(models.Model):
    parent = models.ForeignKey('Category', null=True, blank=True, on_delete=models.CASCADE, related_name="children")
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    nav_image1 = models.ImageField(null=True, blank=True)
    nav_image2 = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.full_name if self.parent else self.name

    @property
    def full_name(self):
        return f"{self.parent} - {self.name}" if self.parent else self.name


@receiver(signals.post_delete, sender=Category)
def delete_image(sender, instance, **kwargs):
    instance.image.delete()
    instance.nav_image1.delete()
    instance.nav_image2.delete()


class Color(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    color = ColorField(default='#FF0000')

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=50)
    color = models.ManyToManyField(Color)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE, limit_choices_to={"children": None})

    def __str__(self):
        return self.title

    @property
    def thumbnails(self):
        thumbnails = []
        for color in self.color.all().values():
            thumbnails.append(dict(image=Image.objects.filter(product__title=self.title, color=color["id"], default=True).values()[0]['image'], color=color["color"]))
        return thumbnails


@receiver(signals.post_delete, sender=Product)
def delete_image(sender, instance, **kwargs):
    instance.image.delete()


class Image(models.Model):
    color = models.ForeignKey(Color, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')
    default = models.BooleanField(default=False)


@receiver(signals.post_delete, sender=Image)
def delete_image(sender, instance, **kwargs):
    instance.image.delete()


class Message(models.Model):
    message = models.CharField(max_length=100)
    link = models.CharField(max_length=200, default=None, null=True, blank=True)

    def __str__(self):
        return self.message


class FeaturedImage(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(null=True, blank=True)
    link = models.CharField(max_length=50, blank=True, null=True)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE,
                                 limit_choices_to={"parent": None})
    category_endorsement_pic = models.BooleanField(default=False, blank=True, null=True)


@receiver(signals.post_delete, sender=FeaturedImage)
def delete_image(sender, instance, **kwargs):
    instance.image.delete()


