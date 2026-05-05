#Excercise 1- Calculate the Area of a rectangle 

# length = float(input("Enter the length of a rectangle"))
# width = float(input("Enter the width of a rectangle"))

# area = length * width
# print(f"The area of the rectangle is {area}cm²")

# Excercise 2 - Shopping Cart Program 

# item  = input("What item Would you like to buy")
# price = float(input("What is the price of the item"))
# quantity = int(input("How many items would you like to buy"))

# total = price * quantity    
# # print(total)
# print(f"You have bought {quantity} X {item}/s")
# print(f"Your total is ₹{total}")


# Madlibs game 

# adjective1 = input("Enter an adjective(description): ")
# noun1 = input("Enter a noun(person, place or thing): ")
# verb1 = input("Enter a verb(ending with ing): ")
# adjective2 = input("Enter another adjective: ")
# adjective3 = input("Enter one more adjective: ")

# print(f"Today I went to a {adjective1} zoo.")
# print(f"In an exhibit, I saw a {noun1}.")
# print(f"{noun1} was {adjective2} and {verb1}.")
# print(f"I was {adjective3}!")


#Strings Excercises
#Excercise-1:- Username is no more than 12 characters
#Excercise-2:- Username must not contain spaces
#Excercise-3:- Username must not contain digits

# username = input("Enter a username: ")

# if len(username) > 12:
#     print("Username must contain less than 12 characters")
# elif not username.find(" ") == -1:
#     print("Username must not contain spaces")
# elif not username.isdigit():
#     print("Username must not contain digits")
# else:
#     print(f"Welcome {username}")