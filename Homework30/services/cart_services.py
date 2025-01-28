# cart_service.py

from models.cart_item import CartItem
from models.product import Product


class CartService:

    @staticmethod
    def view_cart(session):
        cart_items = session.query(CartItem).all()
        if not cart_items:
            print("Cart is empty.")
            return

        for item in cart_items:
            product = session.query(Product).filter(Product.id == item.product_id).first()
            if product:
                print(f"{product.name} (ID: {product.id}) - Quantity: {item.quantity}")

    @staticmethod
    def add_product_to_cart(session, product_id, quantity):
        product = session.query(Product).filter(Product.id == product_id).first()
        if not product:
            print(f"Product with ID {product_id} not found.")
            return

        cart_item = session.query(CartItem).filter(CartItem.product_id == product_id).first()

        if cart_item:
            cart_item.quantity += quantity
            print(f"Updated quantity of {product.name} to {cart_item.quantity}.")
        else:
            new_cart_item = CartItem(product_id=product_id, quantity=quantity)
            session.add(new_cart_item)
            print(f"Added {product.name} (ID: {product.id}) with quantity {quantity} to the cart.")

        session.commit()

    @staticmethod
    def remove_product_from_cart(session, product_id):
        cart_item = session.query(CartItem).filter(CartItem.product_id == product_id).first()

        if not cart_item:
            print(f"Product with ID {product_id} not found in cart.")
            return

        session.delete(cart_item)
        session.commit()
        print(f"Removed product with ID {product_id} from cart.")
