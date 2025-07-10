from enum import Enum


class EnumBase(Enum):

    @classmethod
    def list(cls):
        return list(map(lambda v: v.value, cls))

