import pytest

from core.api.v1.products.filters import ProductFilters
from tests.factories.products import ProductModelFactory
from tests.services.conftest import product_service
from core.apps.products.services.products import IProductService
from core.api.filters import PaginationIn


@pytest.mark.django_db
def test_get_products_count_zero(product_service: IProductService):
    expected_count = 5
    ProductModelFactory.create_batch(size=expected_count)

    products_count = product_service.get_product_count(ProductFilters())
    assert products_count == expected_count

@pytest.mark.django_db
def test_get_products_count_exist(product_service: IProductService):
    products_count = product_service.get_product_count(ProductFilters())
    assert products_count == 0

@pytest.mark.django_db
def test_get_products_all():
    expected_count = 5
    products = ProductModelFactory.create_batch(size=expected_count)
    products_titles = {product.title for product in products}

    fetched_products = product_service.get_product_list(ProductFilters(), PaginationIn())
    fetched_titles = {product.title for product in fetched_products}

    assert len(fetched_products) == expected_count
    assert products_titles == fetched_titles