from ninja import Router, Header
from ninja.errors import HttpError

from core.api.v1.reviews.schemas import CreateReviewSchema, ReviewInSchema, ReviewOutSchema

from core.api.schemas import ApiResponse
from core.apps.common.exceptions import ServiceException
from core.apps.products.containers import get_container
from core.apps.products.services.reviews import IReviewService
from core.apps.products.use_cases.reviews.create import CreateReviewUseCase


router = Router(tags=['Reviews'])


@router.post('{product_id}/review', response=ApiResponse[ReviewOutSchema], operation_id='createReview')
def create_review(
    request,
    product_id: int, 
    schema: ReviewInSchema,
    token: str = Header(alias='Auth-Token'),
) -> ApiResponse[ReviewOutSchema]:
    container = get_container()
    use_case: CreateReviewUseCase = container.resolve(CreateReviewUseCase)
    
    try:
        result = use_case.execute(
            customer_token=token,
            product_id=product_id,
            review=schema.to_entity(),
        )
    except ServiceException as exception:
        raise HttpError(status_code=400, message=exception.message)    
    
    
    return ApiResponse(data=ReviewOutSchema.from_entity(result))
