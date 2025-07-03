from enum import Enum


class GlobalErrorMessage(Enum):
    WRONG_STATUS_CODE = "Received wrong status code"
    WRONG_ELEMENTS_COUNT = "Number of elements is not correct"