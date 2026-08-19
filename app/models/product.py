from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    Float,
    ForeignKey,
    Boolean,
    DateTime
)

from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.database import Base


class Product(Base):

    __tablename__  = "products"

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        index=True
    )

    name = Column(
        String(200),
        nullable=True
    )

    description = Column(
        Text,
        nullable=True
    )

    price = Column(
        Float,
        nullable=False
    )

    stock = Column(
        Integer,
        default=0,
        nullable=False
    )

    is_active = Column(
        Boolean,
        default=True,
        nullable=False
    )

    category_id = Column(
        Integer,
        ForeignKey("categories.id"),
        nullable=False
    )

    brand_id = Column(
        Integer,
        ForeignKey("brands.id"),
        nullable=False
    )

    created_at = Column(
        DateTime,
        server_default=func.now(),
        nullable=False
    )

    updated_at = Column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )


    category = relationship(
        "Category",
        back_populates="products"
    )


    brand = relationship(
        "Brand",
        back_populates="products"
    )

    images = relationship(
        "ProductImage",
        back_populates="product",
        cascade="all, delete-orphan"
    )


