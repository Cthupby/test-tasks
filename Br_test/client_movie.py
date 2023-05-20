from sqlalchemy import Column, String, Integer, Table, ForeignKey
from sqlalchemy.orm import relationship

from base import Base


clients_movies_association = Table(
    'watched_movies', Base.metadata,
    Column('client_id', Integer, ForeignKey('clients.id')),
    Column('movie_id', Integer, ForeignKey('movies.id'))
)


class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String(25))
    genre = Column(String(50))
    year = Column(Integer())
    country = Column(String(50))

    def __init__(self, title, genre, year, country):
        self.title = title
        self.genre = genre
        self.year = year
        self.country = country


class Client(Base):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True)
    name = Column(String(35))
    age = Column(Integer())
    movies = relationship(Movie, secondary=clients_movies_association)

    def __init__(self, name, age):
        self.name = name
        self.age = age
