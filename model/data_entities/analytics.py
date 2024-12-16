from dataclasses import dataclass

@dataclass
class Analytics:
    activityId: str
    activityName: str
    numOfVisitors: int
    rating: int