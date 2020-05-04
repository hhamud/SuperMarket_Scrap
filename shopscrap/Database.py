from sqlalchemy import *
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship 
from scrapy.utils.project import get_project_settings







engine = create_engine("mysql+pymysql://root@localhost/shopscrapdb")

def create_db():
    if not database_exists(engine.url):
        create_database(engine.url)

        print(database_exists(engine.url))


metadata = MetaData()

Base = declarative_base()



association_table = Table(
    'association', Base.metadata,
    Column('name', String, ForeignKey('stock.name')),
    Column('supermarket_name', String, ForeignKey('supermarkets.supermarket_name'))
)

class Stock(Base):
    __tablename__ = 'stock'
    id = Column(Integer, primary_key=True)
    Name =  Column('name',String(50), nullable=False, unique=True)
    Energy =  Column('energy',Integer)
    Carbohydrates =  Column('carbohydrates',Numeric)
    Sugars =  Column('sugars',Numeric)
    Fats =  Column('fats',Numeric)
    Saturates =  Column('saturates',Numeric)
    Protein =  Column('protein',Numeric)
    Fibre =  Column('fibre',Numeric)
    Salt =  Column('salt', Numeric)
    prices = relationship("Prices", backref='Stock')

    

    


class Prices(Base):
    __tablename__ = 'prices'
    id = Column(Integer, primary_key=True)
    Price =  Column('price',Numeric, nullable=False)
    Date =  Column('date', Date)
    stockings = Column(String(50), ForeignKey('stock.name'))



    

class Supermarkets(Base):
    __tablename__ = 'supermarkets'
    id = Column(Integer, primary_key=True)
    supermarket_name =  Column(String(20))
    stock_url =  Column(String(355), unique=True)
    stock_supplier = relationship('Stock', secondary=association_table, backref='stock_name')
    


def connect_db():
    """"
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(get_project_settings().get("CONNECTION_STRING"))

def create_tabele():
    return Base.metadata.create_all(engine, Base.metadata.tables.values(),checkfirst=True)



metadata.create_all(engine)

