from dataclasses import dataclass
from typing import List
from model.data_entities.activity import Activity
from model.data_entities.exposition import Exposition

@dataclass
class Exhibition(Activity):
    expositions: List[Exposition]