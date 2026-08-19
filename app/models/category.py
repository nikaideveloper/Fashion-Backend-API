from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base


class Category(Base):

    __tablename__ = "categories"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
        autoincrement=True
    )

    name = Column(
        String(100),
        nullable=False,
        unique=True
    )

    description = Column(
        String(500),
        nullable=True
    )

    is_active = Column(
        Boolean,
        default=True,
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

    products = relationship(
        "Product",
        back_populates="category"
    )