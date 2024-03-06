from datetime import datetime
from pydantic import BaseModel

from core.apps.products.entities.reviews import Review as ReviewEntity
    

class ReviewInSchema(BaseModel):
    rating: int
    text: str
    
    def to_entity(self):
        return ReviewEntity(rating=self.rating, text=self.text)
    

class CreateReviewSchema(BaseModel):
    product_id: int
    customer_token: int
    review: ReviewInSchema
    
    
class ReviewOutSchema(ReviewInSchema):
    id: int
    created_at: datetime
    updated_at: datetime | None
    
    @classmethod
    def from_entity(cls, review: ReviewEntity) -> 'ReviewInSchema':
        return cls(
            id=review.id,
            text=review.text,
            rating=review.rating,
            created_at=review.created_at,
            updated_at=review.updated_at,
        )
        
        