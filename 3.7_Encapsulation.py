# Encapsulation, protect your data and all the atributes in the object

#---- Client code
# wb = Waterbottle("Contigo", 250)
# print(wb) # Contigo water bottle: 0/250 mL

# wb.contents = 500
# wb.capacity = -9000
# print(wb) # Contigo water bottle: 500/-9000 mL

# ^ not encapsulated

# How to encapsulate
# 1. make attrubites provate
#      you indicate this by putting an _
# 2. make getters and setters
#      geters return a value, setters return none
# 3. provide data validation (if necessary)

class Waterbottle:
    def __init__(self, brand: str, capacity: int) -> None:
        self._brand = brand
        self._capacity = capacity
        self._contents = 0

    def __str__(self) -> str:
        return f"{self._brand} water bottle: {self._contents}/{self._capacity} mL"

    def get_brand(self) -> str:
        return self._brand

    def set_brand(self, brand: str) -> None:
        if len(brand) > 50:
            raise ValueError("Brands name can't exceed 50 characters")
        self._brand = brand

    def get_capacity(self) -> int:
        return self._capacity

    def set_capacity(self, capacity: int) -> None:
        if capacity <= 0:
            raise ValueError("Must be positive")
        self._capacity = capacity

    def get_contents(self) -> int:
        return self._contents

    def set_contents(self, amount: int) -> None:
        if amount > self._capacity:
            raise ValueError(f"This water bottle's contents can't exceed the max of {self._capacity}")
        elif amount < 0:
            raise ValueError(f"Water bottle contents can't be below 0")
        self._contents = amount
    
wb = Waterbottle("Contigo", 250)
print(wb) # Contigo water bottle: 0/250 mL

wb.set_contents(250)
print(wb.get_contents())
print(wb) # Contigo water bottle: 500/-9000 mL
