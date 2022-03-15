from sqlalchemy import Column, DateTime, Integer, Text, text

from ..database import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    surname = Column(Text)
    lastname = Column(Text)
    creation_date = Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=text("(DATETIME('now','localtime'))"),  # XXX SQLite...
    )
