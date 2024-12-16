from flask import flash

from controller.IActivityController import IActivityController
from model.data_entities.activity import Activity
from model.services.activity.ActivityService import ActivityService


class ActivityController(IActivityController):
    def __init__(self):
        self.activityService = ActivityService()

    def createActivity(self, activity: Activity) -> Activity:
        try:
            success = self.auth_service.register(user)
            if success:
                flash("Registration successful!", "success")
                return True
            else:
                flash("Error during registration. Try again.", "error")
                return False
        except Exception as e:
            flash(f"Error: {str(e)}", "error")
            return False

    def getActivity(self, activity_id: str) -> str:
        activity = self.activityService.getActivityById(activity_id)
        return activity.name

    def updateActivity(self, activity: Activity) -> Activity:
        pass

    def deleteActivity(self, name: str):
        activities_list = self.activityService.getActivities()
        for activity in activities_list:
            if activity.name == name:
                activity_id = activity.id
                self.activityService.deleteActivity(activity_id)
                break