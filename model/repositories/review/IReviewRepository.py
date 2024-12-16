from abc import ABC, abstractmethod
from typing import List
from model.data_entities.review import Review


class IReviewRepository(ABC):
    @abstractmethod
    def getReviewsForActivityByActivityId(self, id: str) -> List[Review]:
        pass

    @abstractmethod
    def getReviewById(self, id: str) -> Review:
        pass

    @abstractmethod
    def addReview(self, review: Review):
        pass

    @abstractmethod
    def editReview(self, review: Review):
        pass

    @abstractmethod
    def deleteReview(self, review: Review):
        pass