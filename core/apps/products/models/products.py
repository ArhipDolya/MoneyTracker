from django.db import models

from core.apps.common.models import TimedBaseModel


class Product(TimedBaseModel):
    title = models.CharField(verbose_name='Title of the product', max_length=255)
    description = models.TextField(verbose_name='Description of the product' ,blank=True)
    is_visible = models.BooleanField(verbose_name='Whether the product is in the catalog or not', default=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
