from models.product import Product

def add_sample_data(session):
    products = [
        Product(name="Laptop", price=1000.0, quantity_in_stock=10),
        Product(name="Mouse", price=20.0, quantity_in_stock=50),
        Product(name="Keyboard", price=50.0, quantity_in_stock=30),
    ]

    session.add_all(products)
    session.commit()
    print("Sample data added to the database.")
