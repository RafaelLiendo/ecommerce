from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, DECIMAL, DateTime
from sqlalchemy.orm import relationship

from ..session import Base


class CartProduct(Base):
    __tablename__ = "cart_product"

    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    product_id = Column(Integer, ForeignKey('product.id'), primary_key=True)
    product = relationship("Product")
    quantity = Column(Integer)