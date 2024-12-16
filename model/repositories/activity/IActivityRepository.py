from abc import ABC, abstractmethod
from typing import List
from model.data_entities.activity import Activity


class IActivityRepository(ABC):
    @abstractmethod
    def getActivities(self) -> List[Activity]:
        pass

    @abstractmethod
    def getActivityById(self, id: str) -> Activity:
        pass

    @abstractmethod
    def createActivity(self, activity: Activity):
        pass

    @abstractmethod
    def updateActivity(self, activity: Activity):
        pass

    @abstractmethod
    def deleteActivity(self, activityId: str):
        pass