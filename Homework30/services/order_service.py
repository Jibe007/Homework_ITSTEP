# order_service.py

from datetime import datetime
from models.cart_item import CartItem
from models.product import Product
from models.order import Order
from models.order_item import OrderItem


class OrderService:

    @staticmethod
    def place_order(session):

        cart_items = session.query(CartItem).all()

        if not cart_items:
            print("Cart is empty. Cannot place an order.")
            return

        total_amount = 0
        for item in cart_items:
            product = session.query(Product).filter(Product.id == item.product_id).first()
            if product:
                total_amount += product.price * item.quantity

        order_date = datetime.now()
        order = Order(order_date=order_date, total_amount=total_amount)
        session.add(order)
        session.commit()

        for item in cart_items:
            product = session.query(Product).filter(Product.id == item.product_id).first()
            if product:
                order_item = OrderItem(
                    order_id=order.id,
                    product_id=item.product_id,
                    quantity=item.quantity,
                    price_per_item=product.price
                )
                session.add(order_item)

        session.commit()

        for item in cart_items:
            session.delete(item)
        session.commit()

        print(f"Order placed successfully! Total: {total_amount:.2f}")

    @staticmethod
    def view_orders(session):
        orders = session.query(Order).all()
        if not orders:
            print("No orders found.")
            return

        for order in orders:
            print(f"Order ID: {order.id}, Date: {order.order_date}, Total Amount: {order.total_amount:.2f}")
            order_items = session.query(OrderItem).filter(OrderItem.order_id == order.id).all()
            for item in order_items:
                product = session.query(Product).filter(Product.id == item.product_id).first()
                if product:
                    print(f"  Product: {product.name}, Quantity: {item.quantity}, Price: {item.price_per_item:.2f}")
