from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, DECIMAL, DateTime
from sqlalchemy.orm import relationship

from ..session import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False, index=True)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    cart_products = relationship("CartProduct")
    orders = relationship("Order")
