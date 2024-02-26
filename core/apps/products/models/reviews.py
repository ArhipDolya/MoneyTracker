from django.db import models

from core.apps.common.models import TimedBaseModel


class ProductReview(TimedBaseModel):
    customer = models.ForeignKey(
        to='customers.Customer',
        verbose_name='Reviewer',
        related_name='product_reviews',
    )
    product = models.ForeignKey(
        to='products.Product',
        verbose_name='Product',
        related_name='product_reviews',
    )
    rating = models.PositiveSmallIntegerField(
        verbose_name='User rating',
        default=1,
    )
    text = models.TextField(verbose_name='Review text', blank=True, default='')
    
    class Meta:
        verbose_name = 'Product review'
        verbose_name_plural = 'Product review'
        unique_together = (
            ('customer', 'product'),
        )
