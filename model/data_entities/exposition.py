from dataclasses import dataclass
from typing import List
from model.data_entities.exhibit import Exhibit
from model.data_entities.user import User

@dataclass
class Exposition:
    name: str
    description: str
    creator: User
    exhibits: List[Exhibit]