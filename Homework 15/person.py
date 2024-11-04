class Person:
    def __init__(self, name, deposit=1000, loan=0):
        self.name = name
        self.deposit = deposit
        self.loan = loan

    def __str__(self):
        return f"Saxeli: {self.name}, Deposit: {self.deposit}, Loan: {self.loan}"

    def setDeposit(self, amount):
        if amount < 0:
            print("Ver iqneba uaryofiti")
        else:
            self.deposit = amount
