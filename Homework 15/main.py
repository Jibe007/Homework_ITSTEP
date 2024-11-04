from person import Person
from house import House

seller = Person(name="John smith")
buyer = Person(name="Chelsea rodriguez")

print("Sawyisi detalebi:")
print(seller)
print(buyer)

house = House(id="3141592", price=50000, owner=seller)

print("\nSesxis garesher shesyidva:")
house.sell(buyer)

print("\nSesxis gareshe yidvis shemdeg:")
print(seller)
print(buyer)

# Davabrunot rogorc iyo gayidvamde
house.owner = seller
house.status = "Gasayidi"
seller.setDeposit(1000) #isedac public veli iyo magram mainc

print("------------------AFTER RESET---------------------")
print(seller)
print(buyer)

# Perform a sale with a loan
print("\nSesxit yidva:")
house.sell(buyer, loan_amount=20000)

# Display details after the sale with loan
print("\nSesxit yidvis shemdeg:")
print(seller)
print(buyer)