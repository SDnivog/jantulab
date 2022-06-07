from typing import List, Optional
from pydantic import BaseModel


class BookBase(BaseModel):
    title: str
    description: str

class Book(BookBase):
    class Config():
        orm_mode = True

class User(BaseModel):
    name:str
    email:str
    password:str

class ShowUser(BaseModel):
    name:str
    email:str
    books : List[Book] =[]
    class Config():
        orm_mode = True

class ShowBook(BaseModel):
    title: str
    # issued_count:int
    description:str
    issued_by: ShowUser

    class Config():
        orm_mode = True


class Login(BaseModel):
    username: str
    password:str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
