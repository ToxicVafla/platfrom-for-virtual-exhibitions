from abc import ABC, abstractmethod
from model.data_entities.activity import Activity
from model.data_entities.analytics import Analytics


class IAnalyticsRepository(ABC):
    @abstractmethod
    def getActivityAnalytics(self, activity: Activity) -> Analytics:
        pass