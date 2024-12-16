from dataclasses import dataclass
from model.data_entities.content import Content
from model.data_entities.user import User

@dataclass
class Review:
    id: str
    author: User
    content: Content
    rating: int