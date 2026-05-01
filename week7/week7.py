# class LibraryItem:
#     def __init__(self,title,author,availibility):
#         self.title = title
#         self.author = author
#         self.availibility = availibility
    
#     def check_out(self):
#         if self.availibility:
#             self.availibility = False
#             print(f"{self.title} has been checked out.")
#         else:
#             print(f"{self.title} is currently unavailable.")
    
#     def return_item(self):
#         self.availibility = True
#         print(f"{self.title} has been returned and is now available.")
    
#     def display_info(self):
#         print(f"Title: {self.title}, Author: {self.author}, Availibility: {self.availibility}")
    
# class Book(LibraryItem):
#     def __init__(self, title, author, availibility, genre):
#         super().__init__(title, author, availibility)
#         self.genre = genre
#     def display_info(self):
#         print(f"Title: {self.title}, Author: {self.author}, Availibility: {self.availibility}, Genre: {self.genre}")

# class DVD(LibraryItem):
#     def __init__(self, title, author, availibility, duration):
#         super().__init__(title, author, availibility)
#         self.duration = duration
#     def display_info(self):
#         print(f"Title: {self.title}, Author: {self.author}, Availibility: {self.availibility}, Duration: {self.duration} minutes")

# book = Book("The Great Gatsby", "F. Scott Fitzgerald", True, "Classic")
# dvd = DVD("Inception", "Christopher Nolan", True, 148)
# book.check_out()
# dvd.check_out()
# book.display_info()


from abc import ABC, abstractmethod

class MenuItem(ABC):
    def _init_(self, name, price, availability):
        self.name = name
        self.__price = 0 #private
        self._availability = availability #protected
        
    def get_price(self):
        return self.__price
    
    def set_price(self, price):
        if price >= 0:
            self.__price = price
        else:
            raise ValueError("Price cannot be negative")
    
    @abstractmethod
    def calculate_final_price(self):
        pass
    
class MenuCourse(MenuItem):
    def __init__(self, name, price, availability, service_charge):
        super().__init__(name, price, availability)
        self.service_charge = service_charge
        
    def calculate_final_price(self):
        return self.get_price() + (self.get_price() * self.service_charge)
    
class Desert(MenuItem):
    def __init__(self, name, price, availability, discount):
        super().__init__(name, price, availability)
        self.discount = discount
        
    def calculate_final_price(self):
        return self.get_price() - (self.get_price() * self.discount)

class Drink(MenuItem):
    def __init__(self, name, price, availability, tax):
        super().__init__(name, price, availability)
        self.tax = tax
        
    def calculate_final_price(self):
        return self.get_price() + (self.get_price() * self.tax)

items = [
    MenuCourse("Pasta", 10, True, 0.1),
    Desert("Gulab Jamun", 11, True, 0.2),
    Drink('Coke',14,True,0.3)
    ]           

for item in items:
    print(f"{item.name}: Final Price = {item.calculate_final_price()}")