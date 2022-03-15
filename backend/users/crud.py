from sqlalchemy import select
from sqlalchemy.orm import Session

from . import models, schemas


def get_newest_n_users(db: Session, num: int = 100):
    query = select(models.Users).order_by(models.Users.creation_date.desc()).limit(num)
    return db.execute(query).scalars().all()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.Users(surname=user.surname, lastname=user.lastname)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
