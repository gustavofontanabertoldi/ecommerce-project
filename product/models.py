from django.db import models
from PIL import Image
from django.conf import settings
import os


class Product(models.Model):
    name = models.CharField(max_length=100)
    short_description = models.TextField(max_length=100)
    long_description = models.TextField(max_length=255)
    imagem = models.ImageField(upload_to="product_images/%Y/%m/", blank=True, null=True)
    slug = models.SlugField(unique=True)
    price_marketing = models.FloatField(default=0)
    price_marketing_off = models.FloatField(default=0) #discount
    tipo = models.CharField(
        default='V',
        max_length=1,
        choices=(
            ('V', 'Variação'),
            ('S', 'Simples'),
        ),
    )

    @staticmethod
    def resize_image(img, new_width=800):
        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
        img_pil = Image.open(img_full_path)
        original_width, original_height = img_pil.size

        if original_width <= new_width:
            img_pil.close()
            return

        new_height = round((new_width*original_height) / original_width)
        new_img = img_pil.resize((new_width, new_height), Image.LANCZOS)
        new_img.save(
            img_full_path,
            optmize=True,
            quality = 50
        )
        print("Imagem redimencionada")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        max_image_size = 800

        if self.image:
            self.resize_image(self.image, max_image_size)

    def __str__(self):
        return self.name


class Variation (models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    price = models.FloatField()
    promotional_price = models.FloatField(default=0)
    stock = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name or self.produto.name