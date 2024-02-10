import pytest

from core.api.v1.products.filters import ProductFilters
from tests.factories.products import ProductModelFactory
from tests.services.conftest import product_service
from core.apps.products.services.products import IProductService


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
def test_product_search():
    assert False