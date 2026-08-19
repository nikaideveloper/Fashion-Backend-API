from fastapi import FastAPI
from app.database import engine , Base
from app.routers.user import router as user_router
from app.routers.product_router import router as product_router
from app.routers.admin_product_router import router as admin_product_router
from app.models.product import Product
from app.models.category import Category
from app.models.brand import Brand
from app.models.product_image import ProductImage

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Fashion Backend API"
)


app.include_router(
    user_router,
  prefix="/api/v1"
)

app.include_router(
    admin_product_router,
    prefix="/api/v1"
)

app.include_router(
    product_router,
    prefix="/api/v1"
)

@app.get("/")
def home():
    return {
        "message" : "Fastapi Server is Running"
    }