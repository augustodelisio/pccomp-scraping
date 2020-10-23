from sqlalchemy import create_engine, Column, Table, ForeignKey, MetaData
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Integer, String, Date, DateTime, Float, Boolean, Text)
from scrapy.utils.project import get_project_settings

Base = declarative_base()


def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(get_project_settings().get("CONNECTION_STRING"))


def create_table(engine):
    Base.metadata.create_all(engine)


class Articulo(Base):
    __tablename__ = "articulos"

    id = Column(Integer, autoincrement=True, primary_key=True)
    nombre = Column(String(1000))
    precio = Column(String(50))
    url = Column(String(1000))
    categoria = Column(Integer, ForeignKey('categorias.id'))  # Muchos articulos para una categoria (1 a M)

    def __init__(self, nombre=None, precio=None, url=None, categoria=None):
        self.nombre = nombre
        self.precio = precio
        self.url = url
        self.categoria = categoria


class Categoria(Base):
    __tablename__ = "categorias"

    id = Column(Integer, primary_key=True)
    nombre = Column('nombre', String(50))
    articulos = relationship('Articulo', backref='categorias')  # Una categoria tiene muchos articulos (1 a M)
