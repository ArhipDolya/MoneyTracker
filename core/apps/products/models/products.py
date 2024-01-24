from django.db import models

from core.apps.common.models import TimedBaseModel
from core.apps.products.entities.products import Product as ProductEntity


class Product(TimedBaseModel):
    title = models.CharField(verbose_name='Title of the product', max_length=255)
    description = models.TextField(verbose_name='Description of the product' ,blank=True)
    is_visible = models.BooleanField(verbose_name='Whether the product is in the catalog or not', default=True)

    def to_entity(self) -> ProductEntity:
        return ProductEntity(
            id=self.id,
            title=self.title,
            discription=self.description,
            created_at=self.created_at,
            updated_at=self.updated_at, 
        )

    def __str__(self) -> str:
        return self.title
    
    def __repr__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
