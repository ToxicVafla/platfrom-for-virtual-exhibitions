from abc import ABC, abstractmethod

from model.data_entities.activity import Activity


class IActivityController(ABC):
    @abstractmethod
    def createActivity(self, activity: Activity) -> Activity:
        pass

    @abstractmethod
    def getActivity(self, activity_id: str) -> str:
        pass

    @abstractmethod
    def updateActivity(self, activity: Activity) -> Activity:
        pass

    @abstractmethod
    def deleteActivity(self, name: str):
        pass
