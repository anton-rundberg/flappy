from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from . import __version__, config

Base = declarative_base()

engine = create_engine(
    config.DB_URL,
    connect_args=dict(
        check_same_thread=False,  # XXX Only applicable to SQLite
        # application_name=f"Flappy {__version__}",
    ),
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
