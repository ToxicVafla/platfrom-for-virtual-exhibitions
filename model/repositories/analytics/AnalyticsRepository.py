from typing import List
from model.repositories.analytics.IAnalyticsRepository import IAnalyticsRepository
from model.data_entities.activity import Activity
from model.data_entities.analytics import Analytics


class AnalyticsRepository(IAnalyticsRepository):
    def __init__(self):
        self.analytics = List[Analytics]

    def getActivityAnalytics(self, activity: Activity) -> Analytics:
        for analytic in self.analytics:
            if analytic.activityId == activity.id:
                return analytic