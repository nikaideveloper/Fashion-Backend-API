from fastapi import FastAPI
from app.database import engine , Base
from app.routers.user import router as user_router


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Fashion Backend API"
)


app.include_router(
    user_router
)

@app.get("/")
def home():
    return {
        "message" : "Fastapi Server is Running"
    }