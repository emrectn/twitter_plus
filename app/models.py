from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    password = Column(String(50))
    picture = Column(String(250))
    status = Column(Integer)

    def __repr__(self):
        return '<User(id: {}, username : \'{}\''.format(self.id, self.username)


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    text = Column(String(180))
    user_id = Column(Integer, ForeignKey('users.id'))
    timestamp = Column(Integer, nullable=False)
    user = relationship(User)

# local veritabanı
engine = create_engine('sqlite:///sqlalchemy_database.db')

# tablolar veritabanına kaydedildi.
Base.metadata.create_all(engine)

# Database session oluşturucu oluşturuldu
DBSession = sessionmaker(engine)
# Databasenin o anki oturumunu belirlemeye yarıyor
