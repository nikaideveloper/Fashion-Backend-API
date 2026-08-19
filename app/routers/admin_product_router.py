from fastapi import Depends , APIRouter, status


from sqlalchemy.orm import Session

from app.database import get_db

from app.auth.dependencies import require_admin

from app.models.user import User

from app.schemas.product import ProductCreate,ProductUpdate,ProductResponse

from app.services.product_service import create_product , delete_product_service ,update_product_service


router = APIRouter(
    prefix="/admin/products",
    tags=["Admin Products"]
)


@router.post("/",
             response_model=ProductResponse,
             status_code=status.HTTP_201_CREATED
             )
def add_products(
    data : ProductCreate,
    db : Session = Depends(get_db),
    admin: User = Depends(require_admin)
):
    return create_product(db,data)


@router.delete("/{product_id}")
def delete_product(
    product_id: int,
    db: Session = Depends(get_db),
    admin: User = Depends(require_admin)
):
    delete_product_service(db, product_id)

    return {
        "message": f"Product with id {product_id} deleted successfully"
    }


@router.put(
    "/{product_id}",
    response_model=ProductResponse
)
def update_product_by_id(
    product_id: int,
    data: ProductUpdate,
    db: Session = Depends(get_db),
    admin: User = Depends(require_admin)
):

    return update_product_service(
        db,
        product_id,
        data
    )