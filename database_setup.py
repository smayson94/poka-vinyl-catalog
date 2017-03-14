from sqlalchemy import Column, ForeignKey, Integer, String, LargeBinary
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email =  Column(String(250), nullable=False)
    picture = Column(String(250))

class Genre(Base):
    __tablename__ = 'genre'

    id = Column(Integer, primary_key=True)
    picture_url= Column(String(500))
    name = Column(String(80), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
       """return object data in easily serializeable format"""
       return {
            'name'      :   self.name,
            'id'        :   self.id
       }
    


class Album(Base):
    __tablename__ = 'album'

    id = Column(Integer, primary_key=True)
    catalog_id = Column(String(250)) 
    album_name = Column(String(250),nullable=False)
    picture_url = Column(String(800))
    year = Column(Integer)
    artist = Column(String(250), nullable=False)
    genre_id = Column(Integer,ForeignKey('genre.id'))
    genre = relationship(Genre)
    user_id =  Column(Integer,ForeignKey('user.id'))
    user = relationship(User)

   

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'album_name': self.album_name,
            'id': self.id,
            'artist': self.artist,
            'year': self.year,
            'genre': self.genre_id,
            'picture_url': self.picture_url,
            'catalog_id': self.catalog_id
        }



engine = create_engine('sqlite:///vinylcatalogwithusers.db')


Base.metadata.create_all(engine)