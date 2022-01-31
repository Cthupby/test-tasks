from sqlalchemy import Column, String, Integer, Date

from base import Base


class Client(Base):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    w_movies = Column(String)

    def __init__(self, name, movies):
        self.name = name
        self.w_movies = w_movies
