from ninja import Router

from .schemas import ProductListSchema
from core.apps.products.services.products import IProductService, ORMProductService


router = Router(tags=['Products'])


@router.get('', response=ProductListSchema)
def get_product_list_handler(request) -> ProductListSchema:
    service: IProductService = ORMProductService()
    product_list = service.get_product_list()
    return product_list

