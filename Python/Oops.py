# OOps: Object-Oriented Programming Concepts
#4 Pillars of OOP:- Encapsulation, Abstraction, Inheritance, Polymorphism

# Class:- Blueprints for creating objects. In Python, classes are created using the 'class' keyword.
#Objects:- Instances of classes. They are created using the class constructor and can have attributes (data) and methods (functions) defined by the class.

# class Dog:
#     name = "Jack"
#     breed = "Golden Retriever"

#     def bark(self): #self:- refers to the instance of the class
#         print("Woof!")

#         dog1 = Dog() #Creating an object of the class Dog
#         dog2 = Dog()
#         dog1.bark() #Calling the bark method on the dog1 object
# #         dog2.bark() #Calling the bark method on the dog2 object


# class car:
#     def __init__(self,  model, year, color): #init:- constructor
#         self.model = model
# #         self.year = year
# #         self.color = color

# #     def drive(self):
# #         print(f"You drive the {self.model}.")

# #     def stop(self):
# #         print(f"You stop the {self.model}.")



# # car1 = car("Mustang", 2021, "red")
# # car2 = car("Defender", 2020, "blue")

# # car1.drive()
# # car1.stop()
# # car2.drive()
# # car2.stop()

# # print(car1.model) # Mustang
# # print(car1.year) 
# # print(car1.color) 
    

# #Class variables:- Shared among all instances of class. Defined outside the Constructor
#                 #Allow you to share data among all objects created from that class


# class Student:

#     class_year = 2024
#     num_students = 0

#     def __init__(self, name , age ): #init:- constructor
#         self.name = name
#         self.age = age
#         Student.num_students += 1 # Increment the class variable when a new student is created

# student1 = Student("Harsh Panwar", 20)
# student2 = Student("patrick", 25)
# student3 = Student("John Doe", 22)

# print(student1.name) # Harsh Panwar
# print(student1.age)  # 20
# print(student2.name) # patrick
# print(student2.age)  # 25   

# print(f"My graduating class of {Student.class_year} has {Student.num_students} students.") # My graduating class of 2024 has 3 students.




#--------------------------------E N C A P S U L A T I O N--------------------------------


#1:- Encapsulation: Encapsulation is the bundling of data and the methods that operate on that data within a single unit, or class. It restricts direct access to some of the object's components, which can prevent the accidental modification of data. In Python, encapsulation is achieved through the use of private and protected attributes.

# class BankAccount:
#     def __init__(self, owner, balance): #init:- constructor
#         self.owner = owner #public attribute
#         self._bank = "SBI" #protected attribute
#         self.__balance = balance #private attribute

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"Deposited {amount}. New balance: {self.__balance}")
#         else:
#             print("Invalid deposit amount.")

# #     def withdraw(self, amount):
#         if amount > self.__balance:
#             print("Insufficient funds.")
#         else:
#             self.__balance -= amount
#             print(f"Withdrew {amount}. New balance: {self.__balance}")  

#     def get_balance(self):
#         return self.__balance


# acc = BankAccount("Harsh Panwar", 1000)
# acc.deposit(500) # Deposited 500. New balance: 1500
# acc.withdraw(200) # Withdrew 200. New balance: 1300
# print(acc.get_balance()) # 1300




#----------------------------- I N H E R I T A N C E -----------------------------

#2:- Inheritance:- Allows a class to inherit attributes from another class.Helps with Code Reusablity and extensibilty
                 # Class Child(Parent)
# we use super() to call the parent class's methods and attributes

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def eat(self):
#         print(f"{self.name} is eating")

#     def sleep(self):
#         print(f"{self.name} is sleeping")

#     def breathe(self):
#         print(f"{self.name} is breathing")


# class Dog(Animal):  #Dog Inherits from Animal
#     def __init__(self, name, breed):
#         super().__init__(name) #call the constructor of the parent class(__init__)
#         self.breed = breed

#     def bark(self):
#         print(f"{self.name}, Woof!")

# class Cat(Animal): #Cat Inherits from Animal
#     def meow(self):
#         print(f"{self.name}, Meow!")


# class Bird(Animal): #Bird Inherits from Animal
#     def fly(self):
#         print(f"{self.name} is flying")


# dog = Dog("Jack", "Golden Retriever")
# dog.eat() # Jack is eating.    Inherited from animal
# dog.bark() # Jack, Woof!     Defined in Dog class
# dog.sleep() # Jack is sleeping.  Inherited from animal



#Multiple Inheritane:- A class can inherit from multiple parent classes. This allows a child class to have the attributes and methods of all its parent classes.
# class Animal:
#     def __init__(self, name):
#         self.name = name
#     def eat(self):
#         print(f" {self.name} is eating")

#     def sleep(self):
#         print(f" {self.name} is sleeping")


# class prey(Animal):
#     def flee(self):
#         print("The prey flees from the predator.")

# class predator(Animal):
#     def hunt(self):
#         print("The predator hunts the prey.")

# class Rabbit(prey):
#     pass

# class Hawk(predator):
#     pass

# class Fish(prey, predator): #Fish Inherits from both prey and predator
    # pass


# rabbit = Rabbit("Bugs")
# hawk = Hawk("Tony")
# fish = Fish("Nemo")


# rabbit.eat()
# fish.sleep()





#--------------------------P O L Y M O R P H I S M-----------------------------------

# #Polymorphism:- It means the same method name behave differently for different objects.
# from abc import ABC, abstractmethod

# class Shape:
    
#     @abstractmethod
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#             return 3.14 * self.radius ** 2

# class Square(Shape):
#     def __init__(self, side):
#         self.side = side
    
#     def area(self):
#         return self.side ** 2



# class Triangle(Shape):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height

#     def area(self):
#         return self.base * self.height * 0.5


# class Pizza(Circle):
#     def __init__(self, topping, radius):
#         super().__init__(radius)
#         self.topping = topping
  

# shapes = [Circle(12), Square(5), Triangle(5, 2), Pizza("pepperoni", 15)]


# for shape in shapes:
#     print(f"The area of {shape.area()}")


#Duck Typing: Another way to achieve Polymorphism besides Inheritance 

# class Animal:
#     alive = True

# class Dog(Animal):
#     def speak(self):
#         print("Woof!")

# class Cat(Animal):
#     def speak(self):
#         print("Meow!")


# class Car:
#     alive = False
#     # def horn(self):
#     #     print("Honk!")
#     def speak(self):
#         print("Honk!")

# animals = [Dog(), Cat(), Car()]

# for animal in animals:
#     animal.speak()
#     print(animal.alive)



# class robot:
#     def speak(self):
#         return "beep hopp!"
    
# class human:
#     def speak(self):
#         return "hello there!"
    
# class Parrot:
#     def speak(self):
#         return "Mitthu"

# def make_it_speak(thing):  #Works for any Object
#     print(thing.speak())   #that has speak()

# make_it_speak(robot())
# make_it_speak(human())
# make_it_speak(Parrot())


#----------------------A B S T R A C T I O N -----------------------
# Abstraction:- hides how it works using abstract classes

from abc import ABC, abstractmethod

class Vehicle(ABC):   #abstract class

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def fuel_type(self):
        pass

    def describe(self):     #Normal Method
        print("I'm a vehicle")

class Car(Vehicle):    #must implement both
    def start(self):
        print("Car! Turning Ignition key")

    def fuel_type(self):
        print("Car Runs on petrol")


class Motorbike(Vehicle):
    def start(self):
        print("Press, Power Button")

    def fuel_type(self):
        print("Bike Runs on petrol")

car = Car()
bike = Motorbike()
car.start()
bike.start()
bike.fuel_type()    


