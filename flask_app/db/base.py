from sqlalchemy import Column, Integer, create_engine
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.ext.declarative.base import declared_attr


@as_declarative()
class Base(object):
    engine = create_engine("someengine://...")

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()
    id = Column(Integer, primary_key=True)

    @staticmethod
    def migrate(cls):
        Base.metadata.create_all(bind=cls.engine)
