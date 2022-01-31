from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.orm import relationship

from base import Base


movies_clients_association = Table(
    'movies_clients', Base.metadata,
    Column('movie_id', Integer, ForeignKeyy('movies.id')),
    Column('actor_id', Integer, ForeignKey('actors.id'))
)


class Movie(Base):
    __tablename__ = 'movies'

    id = Colimn(Integer, primary_key=True)
    title = Column(String)
    genre = Column(String)
    year = Column(Integer)
    date = Column(Date)
    clients = relationship("Client", secondary=movies_clients_association)

    def __init__(self, title, genre, year, date):
        self.title = title
        self.genre = genre
        self.year = year
        self.date = date
