from abc import ABC, abstractmethod
from dataclasses import dataclass

from core.apps.products.models.reviews import Review as ReviewDTO

from core.apps.customers.entities import Customer as CustomerEntity
from core.apps.products.entities.products import Product as ProductEntity
from core.apps.products.entities.reviews import Review as ReviewEntity

from core.apps.products.exceptions.reviews import ReviewInvalidRating



class IReviewService(ABC):
    @abstractmethod
    def save_review(self, customer: CustomerEntity, product: ProductEntity, review: ReviewEntity) -> ReviewEntity:
        ...
        

class ORMReviewService(IReviewService):
    def save_review(self, customer: CustomerEntity, product: ProductEntity, review: ReviewEntity) -> ReviewEntity:
        review_dto = ReviewDTO.from_entity(review=review, product=product, customer=customer)
        review_dto.save()
        return review_dto.to_entity()
    

class IReviewValidatorService(ABC):
    def validate(self, review: ReviewEntity, customer: CustomerEntity | None = None, product: ProductEntity | None = None):
        ...
        
        
class ReviewRatingValidatorService(IReviewService):
    def validate(self, review: ReviewEntity, *args, **kwargs):
        if not (1 <= review.rating <= 5):
            raise ReviewInvalidRating(rating=review.rating)
        
        
@dataclass
class ComposedReviewValidatorService(IReviewValidatorService):
    validators: list[IReviewValidatorService]
    
    def validate(self, review: ReviewEntity, customer: CustomerEntity | None = None, product: ProductEntity | None = None):
        for validator in self.validators:
            validator.validate(review=review, customer=customer, product=product)