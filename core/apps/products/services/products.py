from abc import ABC, abstractmethod
from typing import Iterable

from core.apps.products.entities.products import Product


class IProductService(ABC):
    @abstractmethod
    def get_product_list(self) -> Iterable[Product]:
        ...

    @abstractmethod
    def get_product_count(self) -> int:
        ...


class ORMProductService(IProductService):
    ...
    