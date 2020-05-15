from sqlalchemy import *
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship 
from scrapy.utils.project import get_project_settings



metadata = MetaData()

Base = declarative_base()



association_table = Table(
    'association', Base.metadata,
    Column('stock_id', Integer, ForeignKey('stock.id')),
    Column('supermarket_id', Integer, ForeignKey('supermarkets.id')),
    Column('prices_id', Integer, ForeignKey('prices.id')),
)

class Stock(Base):
    __tablename__ = 'stock'
    id = Column(Integer, primary_key=True)
    Name =  Column('name', String(355), nullable=False, unique=True)
    Energy =  Column('energy',String(50))
    Carbohydrates =  Column('carbohydrates',String(10l))
    Sugars =  Column('sugars',String(10))
    Fats =  Column('fats',String(10))
    Saturates =  Column('saturates',String(10))
    Protein =  Column('protein',String(10))
    Fibre =  Column('fibre',String(10))
    Salt =  Column('salt', String(10))



class Prices(Base):
    __tablename__ = 'prices'
    id = Column(Integer, primary_key=True)
    Price =  Column('price', String(10))
    Date =  Column('date', Date)
    stockings = relationship('Stock', secondary=association_table, backref='price_name')

  

class Supermarkets(Base):
    __tablename__ = 'supermarkets'
    id = Column(Integer, primary_key=True)
    name =  Column(String(20))
    stock_url =  Column(String(355), unique=True)
    stock_supplier = relationship('Stock', secondary=association_table, backref='stock_names')
    


def connect_db():
    """"
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(get_project_settings().get("CONNECTION_STRING"))

def create_table(engine):

    return Base.metadata.create_all(engine)



def initialise_database(engine):
    return metadata.create_all(engine, Base.metadata.tables.values(), checkfirst=True)




if __name__ == "__main__":
    engine = connect_db()
    create_table(engine)
    initialise_database(engine)