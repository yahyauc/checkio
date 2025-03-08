#1. Variable Declaration
x = 10          # Integer
y = 3.14        # Float
name = "Hamza"  # String
is_valid = True # Boolean
age: int = 25
pi: float = 3.14

#2. Constant Declaration
PI = 3.14159
MAX_LIMIT = 100

#3. Function Declaration
def greet(name):
    return f"Hello, {name}!"

def add(a: int, b: int) -> int:
    return a + b
  
#4. Class Declaration
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

#5. Method Declaration (Inside a Class)
class Car:
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        print(f"{self.brand} is driving!")


#6. Module and Import Declaration
import math
print(math.sqrt(25))  # 5.0

from math import sqrt
print(sqrt(25))  # 5.0


#7. Lambda Function Declaration
square = lambda x: x ** 2
print(square(5))  # 25

#8. List, Tuple, Dictionary, and Set Declarations
numbers = [1, 2, 3]       # List
coordinates = (10, 20)    # Tuple
person = {"name": "Hamza", "age": 18}  # Dictionary
unique_values = {1, 2, 3} # Set


#9. Exception Handling Declaration
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("Cannot divide by zero!")


# 10. Generator Declaration
def count_up():
    for i in range(5):
        yield i

gen = count_up()
print(next(gen))  # 0
print(next(gen))  # 1


#11. Decorator Declaration
def decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()


#12. Thread Declaration
import threading

def print_hello():
    print("Hello from thread!")

thread = threading.Thread(target=print_hello)
thread.start()

