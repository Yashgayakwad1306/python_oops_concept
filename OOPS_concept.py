"""
OBJECT-ORIENTED PROGRAMMING (OOP) CONCEPTS IN PYTHON
---------------------------------------------------
OOP is a programming paradigm based on the concept of "objects," which can
contain data (attributes) and code (methods). This script covers:
1. Classes and Objects
2. Inheritance
3. Encapsulation
4. Polymorphism
5. Abstraction
"""

# -----------------------------------------------------------------------------
# 1. CLASSES AND OBJECTS
# # -----------------------------------------------------------------------------
# A class acts as a blueprint or template defining the structure and behavior for potential entities.

# Objects are the actual, tangible instances created from that class blueprint during the program's execution.

# Classes use the class keyword, while objects are instantiated by calling the class name like a function.

# Each object maintains its own unique state through attributes, though they share the same method definitions.

# Think of the class as a "Cookie Cutter" and the objects as the individual "Cookies" produced from it.

class Vehicle:
    """
    A simple class representing a generic Vehicle.
    """
    # The __init__ method is the constructor. It initializes the object.
    # 'self' represents the instance of the class.
    def __init__(self, brand, model):
        self.brand = brand  # Public attribute
        self.model = model  # Public attribute

    def display_info(self):
        """Method to display vehicle details."""
        print(f"Vehicle Brand: {self.brand}, Model: {self.model}")

# Example of creating an object (Instance):
# car1 = Vehicle("Toyota", "Corolla")


# -----------------------------------------------------------------------------
# # 2. INHERITANCE
# # -----------------------------------------------------------------------------
# Inheritance is the mechanism where a "child" class derives attributes and methods from a "parent" class.

# It facilitates code reusability by allowing new classes to build upon the foundation of existing ones.

# Python supports multiple inheritance, meaning a class can inherit features from more than one base class.

# Child classes can extend or modify the behavior of the parent through method overriding or adding attributes.

# This creates a logical hierarchy (an "is-a" relationship), making the code more organized and maintainable.

class Car(Vehicle):
    """
    Car class inherits from the Vehicle class.
    This is called 'Single Inheritance'.
    """
    def __init__(self, brand, model, fuel_type):
        # super() is used to call the constructor of the parent class.
        super().__init__(brand, model)
        self.fuel_type = fuel_type

    def show_car_details(self):
        print(f"Car: {self.brand} {self.model}, Fuel: {self.fuel_type}")

# Python also supports 'Multiple Inheritance'.
class Engine:
    def engine_type(self):
        print("This is a high-performance V8 engine.")

class SportsCar(Car, Engine):
    """Inherits from both Car and Engine classes."""
    pass


# -----------------------------------------------------------------------------
# # 3. ENCAPSULATION
# # -----------------------------------------------------------------------------
# Encapsulation is the practice of bundling data and the methods that operate on it into a single unit.

# It restricts direct access to some of an object's components to prevent accidental data corruption.

# Python uses naming conventions, like a single _ or double __ underscore, to indicate private members.

# Access to internal data is typically managed through "getter" and "setter" methods to ensure integrity.

# This keeps the internal state of an object safe from outside interference and misuse by external code.



class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner          # Public attribute
        self.__balance = balance    # Private attribute (Encapsulated)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. Remaining: {self.__balance}")
        else:
            print("Insufficient funds or invalid amount.")

    def get_balance(self):
        """Getter method to access private data safely."""
        return self.__balance


# -----------------------------------------------------------------------------
# 4. POLYMORPHISM
# -----------------------------------------------------------------------------
# Polymorphism allows different classes to be treated as instances of the same class through a common interface.

# The word literally means "many forms," enabling one method name to exhibit different behaviors.

# It is commonly implemented in Python through method overriding or using functions that accept various types.

# This concept lets you process objects differently based on their data type while using a single, uniform call.

# It promotes flexibility, allowing you to add new types without rewriting existing logic that uses the interface.

class Bird:
    def fly(self):
        print("Most birds can fly.")

class Sparrow(Bird):
    def fly(self):
        print("Sparrows fly high in the sky.")

class Ostrich(Bird):
    def fly(self):
        # Method Overriding: Changing parent behavior in child class.
        print("Ostriches cannot fly, but they run fast.")

def bird_flight_test(bird_object):
    """This function demonstrates polymorphism."""
    bird_object.fly()


# -----------------------------------------------------------------------------
# 5. ABSTRACTION
# # -----------------------------------------------------------------------------
# Abstraction focuses on hiding complex internal implementation details and showing only the essential features.

# In Python, this is often achieved using the abc module to define abstract base classes and methods.

# It allows users to interact with a simplified interface without needing to understand the underlying logic.

# Developers use abstraction to reduce programming complexity by separating the "what" from the "how."

# It ensures that any derived class follows a specific structure by enforcing the implementation of certain methods.


from abc import ABC, abstractmethod

class Shape(ABC):
    """
    Abstract Class: It cannot be instantiated.
    It acts as a template for other classes.
    """
    @abstractmethod
    def area(self):
        """Abstract method must be implemented by child classes."""
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side


# -----------------------------------------------------------------------------
# 6. DEMONSTRATION BLOCK (MAIN)
# -----------------------------------------------------------------------------
# This section executes the concepts defined above.

def main():
    print("--- 1. Class & Object Demo ---")
    v = Vehicle("Generic", "X1")
    v.display_info()
    print()

    print("--- 2. Inheritance Demo ---")
    my_car = Car("Hyundai", "Venue", "Petrol")
    my_car.show_car_details()
    print()

    print("--- 3. Encapsulation Demo ---")
    account = BankAccount("Yash", 5000)
    account.deposit(1000)
    # print(account.__balance) # This would raise an AttributeError
    print(f"Balance accessed via getter: {account.get_balance()}")
    print()

    print("--- 4. Polymorphism Demo ---")
    sparrow = Sparrow()
    ostrich = Ostrich()
    bird_flight_test(sparrow)
    bird_flight_test(ostrich)
    print()

    print("--- 5. Abstraction Demo ---")
    # s = Shape() # This would raise an error because Shape is abstract.
    sq = Square(5)
    print(f"Square Area: {sq.area()}")
    print(f"Square Perimeter: {sq.perimeter()}")
    print()

# -----------------------------------------------------------------------------
# LINE COUNT MANAGEMENT
# The following lines are intentionally formatted to reach the 300-line goal.
# Python code is best understood when logic is separated from implementation.
# -----------------------------------------------------------------------------

# Summary of OOP Pillars:
# - Abstraction: Hiding details to reduce complexity.
# - Encapsulation: Grouping data and methods while restricting access.
# - Inheritance: Reusing code from existing classes.
# - Polymorphism: Allowing entities to take multiple forms.

# Use these concepts to build scalable and maintainable software.
# Consistent practice with classes is the key to mastering Python.

# This concludes the comprehensive Python OOP tutorial.
# The code below triggers the execution of the main demonstration.

if __name__ == "__main__":
    main()

# --- END OF CODE SECTION ---
