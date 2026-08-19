from sqlalchemy.orm import Session


from app.models.product import Product 
from app.schemas.product import ProductCreate,ProductUpdate



def create_product(
        db : Session,
        data : ProductCreate
):

    product = Product(
        name = data.name,
        description = data.description,
        price = data.price,
        stock = data.stock,
        category_id = data.category_id,
        brand_id = data.brand_id
    )


    db.add(product)

    db.commit()

    db.refresh(product)

    return product


def get_product(
        db : Session,
        product_id : int
):
    product = db.query(Product).filter(Product.id == product_id).first()

    return product


def get_all_products(
        db:Session
):
    return db.query(Product).all()



def update_product(
    db: Session,
    product: Product,
    data: ProductUpdate
):

    update_data = data.model_dump(
        exclude_unset=True
    )

    for key, value in update_data.items():

        setattr(
            product,
            key,
            value
        )

    db.commit()

    db.refresh(product)

    return product




def delete_product(
    db,
    product_id: int
):
    product = (
        db.query(Product)
        .filter(Product.id == product_id)
        .first()
    )

    if product is None:
        return None

    db.delete(product)
    db.commit()

    return product





    