from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_versioning import version
from sqlalchemy.orm import Session

from ..database import get_db
from . import crud
from .schemas import User, UserCreate

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", response_model=list[User])
@version(1)
def get_newest_five_users(db: Session = Depends(get_db)) -> list[User]:
    db_users = crud.get_newest_n_users(db, 5)
    if db_users is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No users found")
    return db_users


@router.post("/create", response_model=User)
@version(1)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)
