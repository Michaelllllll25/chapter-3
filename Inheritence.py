# arrow for inheritance is the empty triangle
class Animal:
    def __init__(self, name: str, sound: str) -> None:
        self.name = name
        self.sound = sound

    def make_noise(self) -> None:
        print(f"Animal {self.name} says {self.sound}.")

# # dog class is inheriting from animal class
# class Dog(Animal):
#     def __init__(self, name: str) -> None:
#         self.name = name
#         self.sound = "Woof"    # set a defult sound for dogs
        
# super (call init method of the parent and have parent sort out attributes)
class Dog(Animal):
    def __init__(self, name: str) -> None:
        super().__init__(name, "Woof")

    def make_noise(self) -> None:
        print(f"Dog {self.name} says {self.sound}.")    

a = Animal("Bobby", "blah")
a.make_noise()
                                  
d = Dog("Fluffy")
d.make_noise()


#------------------

class Person:
    _MAX_COURSES = 4
   
    def __init__(self, name: str, student_number: str) -> None:
        self._name = name
        self._courses = []

    def set_name(self, name: str) -> None:
        if len(name) > 250:
            raise ValueError("Names must be shorter than 250 characters.")
        self._name = name
    
    def get_name(self) -> str:
        return self._name

    def add_course(self, course: str) -> None:
        if len(self._courses) == self._MAX_COURSES:              
            raise ValueError(f"{self.__class__.__name__} Teachers can only have a maximum of {self._MAX_COURSES} courses.")
        if self.has_course(course):
            raise ValueError(f"{self.__class__.__name__} courses must be unique. Already taking '{course}'.")

        self._courses.append(course)

    def has_course(self, course: str) -> bool:
        return course in self._courses

    def remove_course(self, course: str) -> None:
        if not self.has_course(course):
            raise ValueError(f"{self.__class__.__name__} does not currently have '{course}'.")

class Student(Person):
    def __init__(self, name: str, student_number: str) -> None:
        super().__init__(name)
        self._student_number = student_number

    def get_student_number(self) -> str:
        return self._student_number

class Teacher(Person):
    _MAX_COURSES = 3
    
    def __init__(self, name: str, employee_number: str) -> None:
        super().__init__(name)
        self._employee_number = employee_number

    def get_employee_number(self) -> str:
        return self._employee_number
