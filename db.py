from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from conf import CONNECTION_ROW


class Base(DeclarativeBase):
    pass


engine = create_engine(CONNECTION_ROW)

Session = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)

session = Session()
