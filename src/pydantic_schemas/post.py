from pydantic import BaseModel, field_validator, ValidationError, Field


class PostSchema(BaseModel):
    id: int
    title: str

    @field_validator("id")
    @classmethod
    def validate_id(cls, value: int):
        if value > 10:
            raise ValueError("id must be at least 10")
        return value
