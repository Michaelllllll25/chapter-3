"""
Instance methods- you make a class and crate on aobject, when you crate an oject you are making an instanstance of that class- an object created from a class
a function for an object ^
- Known as behaviours
- Access and/or modify object data
- Functions for objects
"""

class Drink:
    def __init__(self, company: str, name: str, price: float) -> None:
        self.company = company
        self.name = name
        self.price = price
    
    def __str__(self) -> str:
        return f"Drink - {self.company}, {self.name}, {self.price}"

    def set_price(self, new_price: float) -> None:
        if new_price <0:        
            raise ValueError("Price must be positive.")                     # protect the data make sure your only getting a positive number
        self.price = new_price

    def get_product_name(self) -> str:                                              # every instance method MUST start with self
       return f"{self.name} by {self.company}"

    def get_price(self) -> float:
        return self.price

drink1 = Drink("Perk-A-Cola", "Deadshot Daquiri", 4.99)
drink2 = Drink("Huge Corp.", "Copa-Cola", 3.99)

print(drink1)
print(drink2)

drink1.set_price(0.99)
print(drink1.price)

drink2.set_price(1.99)
drink2.price = 1.99      # not good gonna get into it later to protect data(encapsolation)
print(drink2.price)

drink2_name = drink2.get_product_name()
print(drink2_name)

price1 = drink1.get_price()
print(f"Drink1's price is ", price1)
