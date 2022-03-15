from fastapi import FastAPI
from fastapi_versioning import VersionedFastAPI

from . import config
from .database import Base, engine
from .users.route import router as users_router

Base.metadata.create_all(bind=engine)  # Good enough for a demo app


app = VersionedFastAPI(
    FastAPI(
        debug=config.DEBUG,
        title=f"{config.APP_NAME} Backend",
    ),
    version_format="{major}",
    prefix_format="/v{major}",
)

app.include_router(users_router)


if __name__ == "__main__":
    pass
