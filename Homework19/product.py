
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def to_dict(self):

        return {
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity
        }

    def from_dict(data):
        return Product(data["name"], data["price"], data["quantity"])
