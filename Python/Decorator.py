
#using arguments

# def Shout_decorator(func):
#     def wrapper(*args, **kwargs):      #accepts any argument
#         print("Shouting: ", end=" ")
#         result = func(*args, **kwargs)   #passes args through
#         print("Done")
#         return result
#     return wrapper

# @Shout_decorator
# def add(a, b):
#     print(f"{a} + {b} = {a+b}")
#     return a + b

# @Shout_decorator
# def greet(name):
#     print(f"Hello, {name}!")


# add(3,8)
# greet("Harsh")




#The 3 Built-in decorators= @classmethod, @staticmethod, @property

# class Dog:
#     count = 0        #Class Method

#     def __init__(self, name):
#         self.name = name 
#         Dog.count += 1

#     @classmethod
#     def total_dogs(cls):       #cls = The Class Itself
#         print(f"Total Dogs: {cls.count}")

# Dog("Bruno")
# Dog("Jack")
# Dog.total_dogs()



# @property = Decorator used to define a method as a property (it can be accessed like an attribute)
            #  benefit: Add additional logic when read, write, or delete attributes
            #  Gives you getter, setter, and deleter method


# class Rectangle:
#     def __init__(self, width, height):
#         self._width = width
#         self._height = height

#     @property
#     def width(self):
#         return f"{self._width:.1f}cm"

#     @property
#     def height(self):
#         return f"{self.__height:.1f}cm"
    
#     @width.setter
#     def width(self, new_width):
#         if new_width > 0:
#             self._width = new_width
#         else:
#             print("Width must be greater zero")

#     @width.deleter
#     def width(self):
#         del self._width

# rectangle = Rectangle(3, 4)

# # rectangle.width = 2
# # rectangle.height = -1

# del rectangle.width
# # del

# # print(rectangle._width)
# # print(rectangle._height)




#Example

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     @property            #Acess like attribute
#     def area(self):
#         return 3.14 * self.radius ** 2
    
# c = Circle(5)
# property(c.area)