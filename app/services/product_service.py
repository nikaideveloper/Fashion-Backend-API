from sqlalchemy.orm import Session
from fastapi import HTTPException ,status


from app.crud import product
from app.schemas.product import ProductCreate,ProductUpdate



def create_product(
        db : Session,
        data = ProductCreate
):

    create_product = product.create_product(
        db,
        data
    )

    return create_product


def get_all_products(
        db
):
    return product.get_all_products(db)


def get_product(
        db,
        product_id
):
    pro =  product.get_product(db,product_id)

    if pro is None :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )

    return pro



def delete_product_service(
    db,
    product_id: int
):
    deleted_product = product.delete_product(
        db,
        product_id
    )

    if deleted_product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product with id {product_id} not found"
        )

    return deleted_product 





def update_product_service(
    db: Session,
    product_id: int,
    data: ProductUpdate
):

    pro = product.get_product(
        db,
        product_id
    )

    if not pro:

        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return product.update_product(
        db,
        pro,
        data
    )