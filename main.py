from fastapi import FastAPI
from router import item_router
from db.connection import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(item_router.router, prefix="/api/v1", tags=['Items'])


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)