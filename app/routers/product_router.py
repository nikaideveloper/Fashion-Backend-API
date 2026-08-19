from fastapi import Depends , APIRouter, status


from sqlalchemy.orm import Session

from app.database import get_db

from app.auth.dependencies import require_admin

from app.models.user import User

from app.schemas.product import ProductCreate,ProductUpdate,ProductResponse

from app.services.product_service import create_product , get_all_products , get_product

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)



@router.get("/")
def get_products(
    db : Session = Depends(get_db)
):
    return get_all_products(db)


@router.get("/{product_id}")
def get_one_product(
    db : Session = Depends(get_db),
    product_id = int
):
    return get_product(db,product_id)