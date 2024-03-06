import punq

from functools import lru_cache
from core.apps.customers.services.auth import IAuthService, AuthService
from core.apps.customers.services.codes import BaseCodeService, DjangoCacheCodeService
from core.apps.customers.services.customers import ORMCustomerService, ICustomerService
from core.apps.customers.services.senders import BaseSenderService, DummySenderService

from core.apps.products.services.products import ORMProductService, IProductService
from core.apps.products.services.reviews import ComposedReviewValidatorService, IReviewService, IReviewValidatorService, ORMReviewService

from core.apps.products.use_cases.reviews.create import CreateReviewUseCase


@lru_cache(1)
def get_container() -> punq.Container:
    return _initialize_container()
    
    
def _initialize_container() -> punq.Container:
    container = punq.Container()
    # Products
    container.register(IProductService, ORMProductService)
    
    # Customers
    container.register(ICustomerService, ORMCustomerService)
    container.register(BaseCodeService, DjangoCacheCodeService)
    container.register(BaseSenderService, DummySenderService)
    container.register(IAuthService, AuthService)
    container.register(IReviewService, ORMReviewService)
    container.register(IReviewValidatorService, ComposedReviewValidatorService, validators=[])
    container.register(CreateReviewUseCase)
    
    return container