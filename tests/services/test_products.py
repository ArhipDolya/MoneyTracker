import pytest

from tests.services.conftest import product_service
from core.apps.products.services.products import IProductService


@pytest.mark.django_db
def test_products_count(product_service: IProductService):
    assert True

@pytest.mark.django_db
def test_product_search():
    assert False