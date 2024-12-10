from dataclasses import dataclass
from typing import Literal
# pydantic

@dataclass
class MyDice:
    max_score: int
    color: Literal["Red", "Blue"] = "Red"