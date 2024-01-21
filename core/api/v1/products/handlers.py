from ninja import Router

from .schemas import ProductListSchema


router = Router(tags=['Products'])


@router.get('', response=ProductListSchema)
def get_product_list_handler(request) -> ProductListSchema:
    return []

