# aggregation - when you have a custom class that is composed of one or more other classes
# we talk about this as a "has a " relationship
# EX:
# if we create a person class and a bank account class then we can say that a person object has a bank account object
# a Robot object "has a" Motor object
# a Car object "has a" GasTank object

class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

#-


class BankAccount:
    pass


class PersonWithAccount:
    def __init__(self, name: str, age: int, account: BankAccount) -> None:
        self.name = "dave"
        self.age = 45
        self.account = BankAccount()

#-
class GasTank:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.current_volume = capacity

    def add(self, amount: int) -> None:
        self.current_volume += amount

    def consume(self, amount: int) -> None:
        self.current_volume -= amount

    def get_percent_full(self) -> float:
        return self.current_volume / self.capacity

class Brakes:
    def __init__(self, applied: bool, durability: int) -> None:
        self.applied = applied
        self.durability = durability

    def apply(self, drive: bool) -> None:
        print()
        print("On pedal:")
        print(self.applied)
        print("applied")

    def release(self, drive: bool) -> None:
        print()
        print("On pedal:")
        print(self.applied)
        print("released")

    def is_applied(self, drive: bool) -> bool:
        pass

class Car:
    def __init__(self, make: str, model: str, gas_capacity: int):
        self.brakes = Brakes(True, 50)
        self.gas_tank = GasTank(gas_capacity)

    def add_gas(self, amount: int) -> None:
        self.gas_tank.add(amount)

    def get_gas_level(self) -> float:
        return self.gas_tank.get_percent_full()

    def drive(self) -> None:
        print("Driving the car a bit...")
        self.gas_tank.consume(5)

    def stop(self) -> None:
        pass


car1 = Car("Toyota", "Camry", 40)
print(car1.brakes)
print(car1.gas_tank)

print(car1.gas_tank.capacity)
print(car1.gas_tank.current_volume)

(car1.gas_tank.consume(30))
print(car1.gas_tank.current_volume)     # 10


car1.gas_tank.add(10)
print(car1.gas_tank.current_volume)     # 20


car1.add_gas(10)
print(car1.gas_tank.current_volume)     # 30


car1.drive()
print(car1.gas_tank.current_volume)     # 25

print(car1.gas_tank.get_percent_full())   # 0.625
print(car1.get_gas_level())   # 0.625


car2 = Brakes(True, 50)

if car2.applied == True:
    print(car2.apply(car2.applied))   
else:
    print(car2.release(car2.applied))   
