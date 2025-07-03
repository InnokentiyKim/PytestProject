from pydantic import BaseModel, EmailStr, field_validator
from src.enums.user_enums import Gender, Status


class UserSchema(BaseModel):
    id: int
    name: str
    email: str
    gender: Gender
    status: Status

    @field_validator("email")
    def validate_email(cls, email: str) -> str:
        if '@' not in email:
            raise ValueError("Invalid email address")
        return email
