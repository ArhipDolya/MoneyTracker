from dataclasses import field, dataclass

from core.apps.common.enums import EntityStatus

from core.apps.products.entities.products import Product
from core.apps.customers.entities import CustomerEntity


@dataclass
class Review:
    customer: CustomerEntity | EntityStatus = field(EntityStatus.NOT_LOADED)
    product: Product | EntityStatus = field(EntityStatus.NOT_LOADED)
    rating: int = field(default=1)
    text: str = field(default='')