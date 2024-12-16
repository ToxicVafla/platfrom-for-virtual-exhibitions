from dataclasses import dataclass
from model.data_entities.component import Component


@dataclass
class Exhibit(Component):
    image: str # ссылка в строке