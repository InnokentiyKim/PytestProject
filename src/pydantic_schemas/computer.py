from pydantic.types import PastDate, FutureDate, List, PaymentCardNumber
from pydantic.networks import IPv4Address, IPv6Address
from pydantic.color import Color
from pydantic import BaseModel, HttpUrl, UUID4, EmailStr
from src.enums.user_enums import Status


class Physical(BaseModel):
    color: Color
    photo: HttpUrl
    uuid: UUID4

class Owners(BaseModel):
    name: str
    card_number: PaymentCardNumber
    email: EmailStr

class DetailedInfo(BaseModel):
    physical: Physical
    owners: List[Owners]


class Computer(BaseModel):
    status: Status
    activated_at: PastDate
    expiration_at: FutureDate
    host_v4: IPv4Address
    host_v6: IPv6Address
    detailed_info: DetailedInfo