from app.database import Base
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey , Boolean
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from datetime import datetime

class User(Base) :

        __tablename__ = "users"

        id = Column(
            Integer,
            primary_key=True,
            index=True,
            autoincrement=True
        )

        name = Column(
                String(100),
                nullable= False
            )

        email = Column(
                String(255),
                nullable=False,
                unique=True,
                index=True
            )

        password_hash = Column(
                    String(100),
                    nullable=False
                )

        is_active = Column(
                    Boolean,
                    default=True,
                    nullable=False
        )

        role = Column(
                String(20),
                default="customer",
                nullable=False
        )

        
        created_at =  Column(
            DateTime,
            default=datetime.utcnow,
            nullable=False
        )

        updated_at = Column(
            DateTime,
            default=datetime.utcnow,
            onupdate=datetime.utcnow,
            nullable=False
        )
