# from jsonschema import validate

from src.enums.global_enums import GlobalErrorMessage
from src.pydantic_schemas.post import PostSchema
from src.pydantic_schemas.user import UserSchema


class AssertResponse:
    def __init__(self, response):
        self.response = response
        self.schema = None
        self.status = response.status_code
        self.response_data = response.json().get("data") if 'data' in response.json() else response.json()

    def validate(self, schema: type[PostSchema] | type[UserSchema]):
        if isinstance(self.response_data, list):
            for item in self.response_data:
                schema.model_validate(item)
        else:
            schema.model_validate(self.response_data)
        return self

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.status in status_code, GlobalErrorMessage.WRONG_STATUS_CODE.value
        else:
            assert self.status == status_code, GlobalErrorMessage.WRONG_STATUS_CODE.value
        return self


    def __str__(self):
        return str(self.status)
