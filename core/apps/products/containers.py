import punq

from functools import lru_cache
from core.apps.customers.services.auth import BaseAuthService, AuthService
from core.apps.customers.services.codes import BaseCodeService, DjangoCacheCodeService
from core.apps.customers.services.customers import ORMCustomerService, BaseCustomerService
from core.apps.customers.services.senders import BaseSenderService, DummySenderService

from core.apps.products.services.products import ORMProductService, IProductService


@lru_cache(1)
def get_container() -> punq.Container:
    return _initialize_container()
    
    
def _initialize_container() -> punq.Container:
    container = punq.Container()
    # Products
    container.register(IProductService, ORMProductService)
    
    # Customers
    container.register(BaseCustomerService, ORMCustomerService)
    container.register(BaseCodeService, DjangoCacheCodeService)
    container.register(BaseSenderService, DummySenderService)
    container.register(BaseAuthService, AuthService)
    
    return container