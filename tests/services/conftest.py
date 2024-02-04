from core.apps.products.services.products import IProductService, ORMProductService


def product_service() -> IProductService:
    return ORMProductService()