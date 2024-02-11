from django.db import models
from core.apps.common.models import TimedBaseModel


class Customer(TimedBaseModel):
    phone = models.CharField(verbose_name='Phone Number', max_length=16, unique=True)
    token = models.CharField(verbose_name='User Token', max_length=255, unique=True)

    def __str__(self):
        return self.phone
    
    def __repr__(self):
        return self.phone

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'