from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, DECIMAL, DateTime
from sqlalchemy.orm import relationship

from ..session import Base


class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(DECIMAL)