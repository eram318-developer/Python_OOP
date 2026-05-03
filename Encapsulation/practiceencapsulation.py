class Employee:
    def __init__(self,emp_id):
        self._emp_id = emp_id #protected attribute
        self.__salary = 0 #private attribute
    def set_salary(self, salary):
        self.__salary = salary
    
    def get_salary(self):
        return self.__salary
    
    def calculating_bonus(self):
        return self.__salary * 0.1
    
#creating an instance of Employee
employee = Employee(123)
employee.set_salary(20000)
print(f"Employee ID: {employee._emp_id}, Salary: {employee.get_salary()}, Bonus:{employee.calculating_bonus()}") #accessing protected attribute
