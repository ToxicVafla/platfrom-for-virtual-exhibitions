from abc import ABC
from dataclasses import dataclass
from datetime import datetime
from typing import List
from model.data_entities.user import User

@dataclass
class Activity(ABC):
    id: str
    name: str
    theme: str
    description: str
    owner: str
    dateTime: datetime
    participants: List[User]
    rating: int
    reviewIdList: List[str]