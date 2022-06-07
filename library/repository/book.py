from sqlalchemy.orm import Session
from library import models, schemas
from fastapi import HTTPException, status


def get_all(db: Session):
    books = db.query(models.Book).all()
    return books


def create(request: schemas.Book, db: Session):
    new_book = models.Book(title=request.title, description=request.description, user_id=2)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book


def destroy(id: int, db: Session):
    book = db.query(models.Book).filter(models.Book.id == id)

    if not book.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Book with id {id} not found")

    book.delete(synchronize_session=False)
    db.commit()
    return 'done'


def update(id: int, request: schemas.Book, db: Session):
    book = db.query(models.Book).filter(models.Book.id == id)

    if not book.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Book with id {id} not found")

    book.update(request)
    db.commit()
    return 'updated'


def show(id: int, db: Session):
    book = db.query(models.Book).filter(models.Book.id == id).first()
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Book with the id {id} is not available")
    return book
