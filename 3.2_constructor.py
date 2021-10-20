class Employee:
#                       arguements
    def __init__(self, first, last, pay):         # __init__ method can be thought as the constructor
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(emp_1.email)
print(emp_2.email)

print('{} {}'.format(emp_1.first, emp_1.last))

##################################### Gallos video

# class Waterbottle:
#     brand: str
#     volume: int
#     colour: str

# wb = Waterbottle()
# wb.brand = "Contigo"
# wb.volume = 750
# wb.colour = "blue"

# print(f"My {wb.colour} {wb.brand} water bottle")
# print(f"holds {wb.volume} ml of liquid.")

##### new

class Waterbottle:                   # first parameter always self
    def __init__(self, brand: str, volume: int, colour: str) -> None:
        print("Created water bottle object")
        print(brand)
        print(volume)
        print(colour)
        self.product_id = 12345
        self.brand = brand
        self.volume = volume
        self.colour = colour

wb = Waterbottle("Contigo", 750, "blue")

print(wb.product_id)

print(f"My {wb.colour} {wb.brand} water bottle")
print(f"holds {wb.volume} ml of liquid.")

################### ~~~~~~~

class Student:
    def __init__(self, name: str, grade: int) -> None:
        self.name = name
        self.grade = grade
        
student = Student("Michael", 12)

print(f"{student.name} is in grade {student.grade}")


