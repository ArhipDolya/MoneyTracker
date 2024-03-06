from dataclasses import field, dataclass
from datetime import datetime

from core.apps.common.enums import EntityStatus

from core.apps.products.entities.products import Product
from core.apps.customers.entities import CustomerEntity


@dataclass
class Review:
    id: int | None = field(default=None, kw_only=True)
    customer: CustomerEntity | EntityStatus = field(EntityStatus.NOT_LOADED)
    product: Product | EntityStatus = field(EntityStatus.NOT_LOADED)
    
    rating: int = field(default=1)
    text: str = field(default='')
    
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = field(default=None)
    