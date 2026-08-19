from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Boolean,
    DateTime
)

from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.database import Base


class ProductImage(Base):

    __tablename__ = "product_images"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
        autoincrement=True
    )

    product_id = Column(
        Integer,
        ForeignKey("products.id"),
        nullable=False
    )

    image_url = Column(
        String(500),
        nullable=False
    )

    is_primary = Column(
        Boolean,
        default=False,
        nullable=False
    )

    created_at = Column(
        DateTime,
        server_default=func.now(),
        nullable=False
    )

    product = relationship(
        "Product",
        back_populates="images"
    )