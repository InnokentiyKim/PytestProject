from enum import Enum
from src.baseclasses.enum_base import EnumBase


class Gender(Enum):
    female = "female"
    male = "male"


class Status(EnumBase):
    active = "active"
    inactive = "inactive"
    unknown = "unknown"