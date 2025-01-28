

from database.db_connection import Session, initialize_database
from services.cart_services import CartService
from services.order_service import OrderService
from utils.sample_data import add_sample_data


def main():
    initialize_database()

    session = Session()

    add_sample_data(session)

    while True:
        print("\nChoose an action:")
        print("1. View Cart")
        print("2. Add Products to Cart")
        print("3. Remove Products from Cart")
        print("4. Place Order")
        print("5. View Orders")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            CartService.view_cart(session)
        elif choice == "2":
            product_id = int(input("Enter product ID: "))
            quantity = int(input("Enter quantity: "))
            CartService.add_product_to_cart(session, product_id, quantity)
        elif choice == "3":
            product_id = int(input("Enter product ID to remove: "))
            CartService.remove_product_from_cart(session, product_id)
        elif choice == "4":
            OrderService.place_order(session)
        elif choice == "5":
            OrderService.view_orders(session)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
