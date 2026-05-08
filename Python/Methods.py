# # static method: A Method that belong to a class rather than any object from that class(instance) Usually used for general Utility functions.


# # Instance Methods = best for operations on instances of the class (objects)
# # Staic Method = Best for utility function that do not need access to class data.


# # class Employee:

# #     def __init__(self, name, position):
# #         self.name = name
# #         self.position = position

# #     def get_info(self):    #Instance Method
# #         return f"{self.name} = {self.position}"
    
# #     @staticmethod
# #     def is_valid_position(position):
# #         valid_position =  ["Manger", "Cashier", "Cook", "Janitor"]
# #         return position in valid_position
    
# # employee1 = Employee("Harsh", "Manager")
# # employee2 = Employee("Sponge", "Janitor")
# # employee3 = Employee("jack", "Cashier")

# # Employee.is_valid_position("Cook")

# # print(employee1.get_info())
# # print(employee2.get_info())
# # print(employee3.get_info())




# #Class Methods:- Allows operations related to the class itself 
#                 # Take (self) as the first parameter, which represents the class itself

# # class Student:

# #     count = 0
# #     total_gpa = 0

# #     def __init__(self, name, gpa):
# #         self.name = name
# #         self.gpa = gpa
# #         Student.count += 1
# #         Student.total_gpa += gpa


# #     def get_info(self):
# #         return f"{self.name} = {self.gpa}"
    
# #     @classmethod
# #     def get_count(cls):
# #         return f"Total Number of students: {cls.count}"
    
# #     @classmethod
# #     def get_average_gpa(cls):
# #         if cls.count == 0:
# #             return 0
# #         else:
# #             return f"{cls.total_gpa / cls.count}"
    

# # student1 = Student("Spongebob", 3.2)
# # student1 = Student("Patric", 2.2)
# # student1 = Student("Sandy", 4.0)

# # print(Student.get_count())
# # print(Student.get_average_gpa())


# #Magic Methods = Dunder methods (double underscore) __init__, __str__, __eq__
#             #    They are automatically callled by many of pythons's built-in operations.
#             #    They are allow developers to define or customize the behavior of objects

# class Book:

#     def __init__(self, title, author, num_pages):
#         self.title = title
#         self.author = author
#         self.num_pages = num_pages

#     def __str__(self):      #STrings
#         return f"'{self.title}' by {self.author}"
    
#     def __eq__(self, other):       #equality
#         return self.title == other.title and self.author == other.author
    
#     def __lt__(self, other):    #Less than 
#         return self.num_pages < other.num_pages
    
#     def __contains__(self, keyword):
#         return keyword in self.title or keyword in self.author
    
#     def __getitem__(self, key):
#         if key == "title":
#          return self.title
#         elif key == "author":
#             return self.author
#         elif key == "num_pages":
#             return self.num_pages
#         else:
#             return f"key {key} was not found"


# book1 = Book("The Hobbit", "J.R.R Tokien", 310)
# book2 = Book("Harry Potter", "J.K Rowling", 223)
# book3 = Book("The Lion, The Wtch and the wardrobe", "C.S. Lewis", 172)

# print(book1)
# print(book2)
# print(book3)
# print(book1['author'])

# print(book2 == book1)
