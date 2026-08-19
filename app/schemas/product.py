from pydantic import BaseModel , ConfigDict


class ProductCreate(BaseModel):

    name : str

    description : str

    price : float

    stock : int

    category_id : int

    brand_id : int



class ProductUpdate(BaseModel):

    name: str | None = None

    description: str | None = None

    price: float | None = None

    stock: int | None = None

    category_id: int | None = None

    brand_id: int | None = None



class ProductResponse(BaseModel):

    id: int

    name: str

    description: str | None

    price: float

    stock: int

    category_id: int

    brand_id: int

    is_active: bool

    model_config = ConfigDict(
        from_attributes=True
    )