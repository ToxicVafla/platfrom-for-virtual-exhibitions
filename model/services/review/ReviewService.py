from typing import List
from model.data_entities.activity import Activity
from model.data_entities.review import Review
from model.services.review.IReviewService import IReviewService
from model.repositories.review.ReviewRepository import ReviewRepository


class ReviewService(IReviewService):
    def __init__(self):
        self.reviewRepository = ReviewRepository()

    def getReviewsForActivity(self, activity: Activity) -> List[Review]:
        return self.reviewRepository.getReviewsForActivityByActivityId(activity.id)

    def getReviewById(self, id: str) -> Review:
        return self.reviewRepository.getReviewById(id)

    def addReview(self, review: Review):
        self.reviewRepository.addReview(review)

    def editReview(self, review: Review):
        self.reviewRepository.editReview(review)

    def deleteReview(self, review: Review):
        self.reviewRepository.deleteReview(review)