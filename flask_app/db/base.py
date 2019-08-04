from sqlalchemy import Column, Integer, create_engine
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.ext.declarative.base import declared_attr


def prepare_connection_str(app):
    print(app.config)
    t = f"{app.config['SQLALCHEMY_DB_DIALECT']}://{app.config['SQLALCHEMY_DB_USERNAME']}:{app.config['SQLALCHEMY_DB_PASSWORD']}@{app.config['SQLALCHEMY_DB_HOST']}:{app.config['SQLALCHEMY_DB_PORT']}/{app.config['SQLALCHEMY_DB_NAME']}"
    print(t)
    return t

@as_declarative()
class Base(object):

    #
    # def __init__(self, app):
    #     engine = create_engine("someengine://...")
    #     print(vars(app))

    # @declared_attr
    # def __tablename__(cls):
    #     return cls.__name__.lower()
    id = Column(Integer, primary_key=True)


    @staticmethod
    def migrate(cls, flask_app):
        print(vars(flask_app))
        cls.engine = create_engine(prepare_connection_str(flask_app))
        Base.metadata.create_all(bind=cls.engine)


