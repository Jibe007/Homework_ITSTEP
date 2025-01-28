from sqlalchemy import Column, Integer, DateTime, Float
from database.db_connection import Base

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_date = Column(DateTime, nullable=False)
    total_amount = Column(Float, nullable=False)
