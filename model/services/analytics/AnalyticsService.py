from model.data_entities.activity import Activity
from model.data_entities.analytics import Analytics
from model.services.analytics.IAnalyticsService import IAnalyticsService
from model.repositories.analytics.AnalyticsRepository import AnalyticsRepository


class AnalyticsService(IAnalyticsService):
    def __init__(self):
        self.analyticsRepository = AnalyticsRepository()

    def getActivityAnalytics(self, activity: Activity) -> Analytics:
        return self.analyticsRepository.getActivityAnalytics(activity)