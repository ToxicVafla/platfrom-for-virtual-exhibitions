from typing import List, Dict
from model.repositories.review.IReviewRepository import IReviewRepository
from model.data_entities.review import Review


class ReviewRepository(IReviewRepository):
    def __init__(self):
        self.reviews: Dict[str, Review] = {}

    def getReviewsForActivityByActivityId(self, id: str) -> List[Review]:
        return [review for review in self.reviews.values() if review.id == id]

    def getReviewById(self, id: str) -> Review:
        return self.reviews.get(id)

    def addReview(self, review: Review):
        if review.id not in self.reviews:
            self.reviews[review.id] = review
        else:
            raise ValueError(f"Review with id {review.id} already exists.")


    def editReview(self, review: Review):
        if review.id in self.reviews:
            self.reviews[review.id] = review
        else:
            raise ValueError(f"Review with id {review.id} does not exist.")


    def deleteReview(self, review: Review):
        if review.id in self.reviews:
            del self.reviews[review.id]
        else:
            raise ValueError(f"Review with id {review.id} does not exist.")