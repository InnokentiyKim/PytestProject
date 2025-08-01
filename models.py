from sqlalchemy import Integer, String, Boolean, Column
from db import Base


class Films(Base):
    __tablename__ = 'films'

    film_id = Column(Integer, primary_key=True)
    status = Column(String, index=True)
    title = Column(String)
    is_premiere = Column(Boolean)

