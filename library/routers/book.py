from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from library import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from library.repository import book

router = APIRouter(
    prefix="/book",
    tags=['My Books']
)

get_db = database.get_db


@router.get('/', response_model=List[schemas.ShowBook])
def all(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return book.get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED,)
def create(request: schemas.Book, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return book.create(request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return book.destroy(id, db)


# @router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
# def update(id: int, request: schemas.Book, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
#     return book.update(id, request, db)


@router.get('/{id}', status_code=200, response_model=schemas.ShowBook)
def show(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return book.show(id, db)
