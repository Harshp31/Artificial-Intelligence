# Immutable Data Types

# 1. Integers
# x = 5
# x = x + 10
# print(x) #15

# 2. Floating Point Numbers
# y = 5.5
# y = y + 1.5
# print(y) #7.0

# 3. Strings
# name = "Alice"
# name = name + " Smith"
# print(name) #"Alice Smith"

# 4. Bytes
# data = b"Hello"
# data = data + b" World"
# print(data) #b"Hello World"


# 5. Tuples (ordered and unchangeable)

# tuple1 = (1, 2, 3)
# t2 = ("a", "b", "c")
# t3 = (1, 1,  "a", 3.14)

# # print(tuple1)
# # print(t2[0]) #a. Accesing elements
# # print(t3[0:2]) #(1, "a")  Slicing

# #Tuple Methods

# print(t3.count(1)) #Counts number of occurrences of 1
# print(t2.index("b")) #Finds index of "b"

# fruits = ("apple", "banana", "cherry", "coconut", "coconut")

# # print(dir(fruits)) #List of all methods available for tuples
# # print(help(fruits.count)) #Documentation for count method
# print(len(fruits)) #Length of the tuple
# print("cherry" in fruits) #Check if "cherry" is in the tuple
# print(fruits.count("coconut")) #Counts number of occurrences of "coconut"



# TypeCasting

# name = "Py Python"
# age = 25
# gpa = 3.8
# is_student =True

# name = bool(name)
# print(name) #True
# print(type(name))
# print(type(age))
# print(type(gpa))
# print(type(is_student))

# print(int(gpa))

# age = float(age)
# age = str(age)
# age += "1"
# print(age)
# print(age)

# age += 1
# print(age)


# User Input

# name = input("What is your name: ")
# # age = input("What is your age: ")
# # age = int(age) #Typecasting age to integer
# # age += 1 #Incrementing age by 1

# age = int(input("What is your age: ")) #Combining input and typecasting in one line
# age += 1 #Incrementing age by 1

# # print("Hello, " + name + "!")

# print(f"Hello {name}!")
# print("HAPPY BIRTHDAY!")
# print(f"You are {age} years old.")

#Encryption 
import random
import string


chars = " " + string.punctuation + string.digits + string.ascii_letters 
chars = list(chars)
key = chars.copy()

random.shuffle(key)

#Encrypt
plain_text = input("Enter text to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f'Encrypted text: {cipher_text}')

