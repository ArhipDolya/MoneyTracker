from dataclasses import dataclass
from datetime import datetime


@dataclass()
class Product:
    title: str
    discription: str
    created_at: datetime
    updated_at: datetime
