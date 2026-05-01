# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
#     def eat(self):
#             print("The Animal is eating")
            
# class Cat(Animal):
#     def __init__(self, name, age, color):
#         super().__init__(name, age)
#         self.color = color

#     def eat(self):
#         super().eat()  # Call the eat method of the parent class
#         print("The Cat is eating")        

# myCat = Cat("Whiskers", 5, "Gray")
# print(f"Name: {myCat.name}, Age: {myCat.age}, Color: {myCat.color}")
# myCat.eat()


class Employee:
    def __init__(self,name, employee_id):
        self.name = name
        self.employee_id = employee_id
    
class Department:
    def __init__(self, department, location):
        self.department = department
        self.location = location

class Manager(Employee, Department):
    def __init__(self, name, employee_id, department, location,title):
        Employee.__init__(self, name, employee_id)
        Department.__init__(self, department, location)
        self.title = title
    def display_info(self):
        print(f"Name: {self.name}, Employee ID: {self.employee_id}, Department: {self.department}, Location: {self.location}, Title: {self.title}")
    
    
manager = Manager("Alice", "E123", "HR", "New York", "HR Manager")
manager.display_info()