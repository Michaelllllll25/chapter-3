student1 = {
    "name": "Jeff Smith",
    "grade": 9
}

student2 = {
    "name": "Holly Staples",
    "grade": 10
}

print(student1["name"])
print(student1["grade"])

# ---------- transform to classes
#                                                  Uml- UNIFIED MODELING LANGUAGE

class Student:
    name: str
    grade: int

student1 = Student()                   # create an object
student1.name = "Jeff Smith"
student1.grade = 99

student2 = Student()                   # create an object
student2.name = "Holly Staples"
student2.grade = 10

print(student1.name)
print(student1.grade)

print(student2.name)
print(student2.grade)
# --------------------------------

class Waterbottle:
    volume: int
    colour: str
    brand: str

bottle1 = Waterbottle()
bottle1.volume = 100
bottle1.colour = "black"
bottle1.brand = "nestle"

bottle2 = Waterbottle()
bottle2.volume = 200
bottle2.colour = "yellow"
bottle2.brand = "coca cola"


print(bottle1.volume)     # alt + command/cntrl down dwon to edit more
print(bottle1.colour)
print(bottle1.brand)
print()
print(bottle2.volume)
print(bottle2.colour)
print(bottle2.brand)

################################################### VIDEO
## create and use classes

class Employee:
    pass

emp_1 = Employee()
emp_2 = Employee()

emp_1.first = 'Corey'
emp_1.last = 'Schafer'
emp_1.email = 'Corey.Schafer@company.com'
emp_1.pay = 50000

emp_2.first = 'Test'
emp_2.last = 'User'
emp_2.email = 'Test.User@company.com'
emp_2.pay = 60000

print(emp_1.email)
print(emp_2.email)

    
