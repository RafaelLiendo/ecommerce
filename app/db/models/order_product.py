from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, DECIMAL, DateTime
from sqlalchemy.orm import relationship

from ..session import Base


class OrderProduct(Base):
    __tablename__ = "order_product"

    order_id = Column(Integer, ForeignKey('order.id'), primary_key=True)
    product_id = Column(Integer, ForeignKey('product.id'), primary_key=True)
    product = relationship("Product")
    quantity = Column(Integer)
    subtotal = Column(DECIMAL)
