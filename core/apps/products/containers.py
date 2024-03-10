import punq

from functools import lru_cache
from logging import Logger, getLogger

from core.apps.customers.services.auth import IAuthService, AuthService
from core.apps.customers.services.codes import BaseCodeService, DjangoCacheCodeService
from core.apps.customers.services.customers import ORMCustomerService, ICustomerService
from core.apps.customers.services.senders import BaseSenderService, DummySenderService

from core.apps.products.services.products import ORMProductService, IProductService
from core.apps.products.services.reviews import ComposedReviewValidatorService, IReviewService, IReviewValidatorService, \
                                                ORMReviewService, ReviewRatingValidatorService, SingleReviewValidatorService

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
    container.register(SingleReviewValidatorService)
    container.register(ReviewRatingValidatorService)
    container.register(Logger, factory=getLogger, name='elasticapm.errors')
    
    def build_validator(container: punq.Container) -> IReviewValidatorService:
        return ComposedReviewValidatorService(validators=[
            container.resolve(SingleReviewValidatorService),
            container.resolve(ReviewRatingValidatorService),
        ])
        
    container.register(IReviewValidatorService, factory=build_validator)
    
    container.register(CreateReviewUseCase)
    
    return container