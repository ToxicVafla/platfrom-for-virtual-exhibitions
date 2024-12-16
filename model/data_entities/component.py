from abc import ABC
from dataclasses import dataclass

@dataclass
class Component(ABC):
    id: str
    name: str
    description: str
    creator: str