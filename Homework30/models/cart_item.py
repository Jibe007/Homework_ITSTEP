from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database.db_connection import Base

class CartItem(Base):
    __tablename__ = 'cart_items'

    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False)

    product = relationship("Product", backref="cart_items")
