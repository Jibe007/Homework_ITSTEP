class House:
    def __init__(self, id, price, owner):
        self.id = id
        self.price = price
        self.owner = owner
        self.status = "Gasayidi"

    def sell(self, buyer, loan_amount=None):
        if loan_amount is None:
            self.owner.deposit += self.price
            self.owner = buyer
            self.status = "Gayiduli"
            print(f"Saxli {self.id} sheisyida {buyer.name}  {self.price}GEL-ad. Status: {self.status}")
        else:
            self.owner.deposit += self.price
            self.owner = buyer
            self.status = "Gayiduli sesxit"
            buyer.loan += loan_amount
            print(f"Saxli {self.id} sheisyida {buyer.name} sesxit: {loan_amount}GEL. Status: {self.status}")