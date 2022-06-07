from email.policy import default
from sqlalchemy import Column, Integer, String, ForeignKey
from library.database import Base
from sqlalchemy.orm import relationship


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    # issued_count = Column(Integer, default="3")
    user_id = Column(Integer, ForeignKey('users.id'))

    issued_by = relationship("User", back_populates="books")


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    books = relationship('Book', back_populates="issued_by")


# class BookInventry(Base):
#     __tablename__ = 'books'

#     id = Column(Integer, primary_key=True, index=True)
#     inventry_title = Column(String)

