# 3.4 Instance Methods
# function for objects
# access and/or modify object state

# UML CODE
#            Drink
# ----------------------------
# brand: str
# name: str
# volume: int
# max_volume: int
# ----------------------------
# Drink(str, str, int)               # senf Drink class brand, new, volume
# get_display_name() -> str          # get_display_name (method)
# fill(int) -> None
# consume(int) -> None
# ----------------------------

class Drink:
    def __init__(self, brand: str, name: str, volume: int):
        self.brand = brand
        self.name = name
        self.volume = volume
        self.max_volume = volume
    
    def get_display_name(self):
        return f"{self.name} by {self.brand}"

    def get_name(self) -> str:
        return self.name

    def get_brand(self) -> str:
        return self.brand

    def consume(self, amount: int) -> None:
#       self.volume -= amount   
        self.volume = max(self.volume - amount, 0)   # capping at 0

    def fill(self, amount: int) -> None:
        self.volume = min(self.volume + amount, self.max_volume)



my_drink = Drink("Perk-A-Cola", " Deadshot Daquiri", 350)
drink2 = Drink("Huge Corp.", "Popular Drink", 500)

result = my_drink.get_display_name()
print(result)

result = drink2.get_display_name()
print(result)

# my_drink.consume(100)
# print(my_drink.volume)   # returns 250

# my_drink.consume(500)
# print(my_drink.volume)   # returns 0

my_drink.consume(100)
print(my_drink.volume)     # returns 250

my_drink.fill(1000)            
print(my_drink.volume)     # 350 (it is capped off to 350 max)

# my_drink.consume(100)
# my_drink.fill(1000)         
