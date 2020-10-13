from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, DECIMAL, DateTime
from sqlalchemy.orm import relationship

from ..session import Base


class Order(Base):
    __tablename__ = "order"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    date = Column(DateTime)
    total = Column(DECIMAL)
    order_products = relationship("OrderProduct")
