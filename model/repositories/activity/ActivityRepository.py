from typing import List
from typing import Dict
from model.data_entities.activity import Activity
from model.repositories.activity.IActivityRepository import IActivityRepository

class ActivityRepository(IActivityRepository):
    def __init__(self):
        self.activities: Dict[str, Activity] = {}

    def getActivities(self) -> List[Activity]:
        return list(self.activities.values())

    def getActivityById(self, id: str) -> Activity:
        return self.activities.get(id)

    def createActivity(self, activity: Activity):
        if activity.id not in self.activities:
            self.activities[activity.id] = activity
        else:
            raise ValueError(f"Activity with ID {activity.id} already exists.")

    def updateActivity(self, activity: Activity):
        if activity.id in self.activities:
            self.activities[activity.id] = activity
        else:
            raise ValueError(f"Activity with ID {activity.id} does not exist.")

    def deleteActivity(self, id: str):
        if id in self.activities:
            del self.activities[id]
            print(f"Activity with ID {id} deleted.")
        else:
            print(f"Activity with ID {id} not deleted.")
            raise ValueError(f"Activity with ID {id} does not exist.")