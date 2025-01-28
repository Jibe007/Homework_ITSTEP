from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = 'postgresql+psycopg2://postgres:12345@localhost:5432/postgres'

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()

def initialize_database():
    from models.product import Product
    from models.cart_item import CartItem
    from models.order import Order
    from models.order_item import OrderItem

    # Create tables
    Base.metadata.create_all(engine)
    print("Database initialized: tables created successfully.")
