from typing import List
from model.data_entities.activity import Activity
from model.repositories.activity.ActivityRepository import ActivityRepository
from model.services.activity.IActivityService import IActivityService


class ActivityService(IActivityService):
    def __init__(self):
        self.repository = ActivityRepository()

    def getActivities(self) -> List[Activity]:
        return self.repository.getActivities()

    def getActivityById(self, id: str) -> Activity:
        return self.repository.getActivityById(id)

    def createActivity(self, activity: Activity):
        return self.repository.createActivity(activity)

    def updateActivity(self, activity: Activity):
        return self.repository.updateActivity(activity)

    def deleteActivity(self, activityId: str):
        return self.repository.deleteActivity(activityId)