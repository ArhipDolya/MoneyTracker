from abc import ABC, abstractmethod
from typing import Iterable

from core.apps.products.entities.products import Product
from core.apps.products.models.products import Product as ProductDTO


class IProductService(ABC):
    @abstractmethod
    def get_product_list(self) -> Iterable[Product]:
        ...

    @abstractmethod
    def get_product_count(self) -> int:
        ...


class ORMProductService(IProductService):
    def get_product_list(self) -> Iterable[Product]:
        qs = ProductDTO.objects.filter(is_visible=True)

        return [product.to_entity() for product in qs]
    