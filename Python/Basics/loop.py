#While loop

# name = input("Enter your name: ")

# while name == "":
#     print("You did not enter your name.")
#     name = input("Please enter your name: ")

# print(f"Hello, {name}!")


# food = input("Enter your favorite food(q to quit): ")

# # while not  food.lower() == "q":

# while  food.lower() != "q":
#     print(f"Your favorite food is {food}")
#     food = input("Enter your another favorite food(q to quit): ")

# print("Bye!")




# Compound Interest Calculator

# principle = 0
# rate = 0
# time = 0


# while principle <= 0:
#     principle = float(input("Enter the principle amount: "))
#     if principle <= 0:
#         print("Please enter a valid principle amount.")

# while rate <= 0:
#     rate = float(input("Enter the rate of interest: "))
#     if rate <= 0:
#         print("Please enter a valid rate of interest.")

# while time <= 0:
#     time = int(input("Enter the time (in years): "))
#     if time <= 0:
#         print("Please enter a valid time (in years).")

# total_amount = principle * pow((1 + rate/100), time)
# print(f"Total amount after {time} years: ₹{total_amount:.2f}")



# For Loops

# for x in range(1, 11):
# for x in range(1, 11, 2):
#     print(x)


# credit_card = "1234-5678-9012-3456"
# for x in credit_card:
#     print(x)

# for x in range(1, 21):
#     if x == 13:
#         continue
#     else:
#         print(x)

# for x in range(1, 21):
#     if x == 13:
#         break
#     else:
#         print(x)

# for x in range(4):
#     print(x)
# else:
#     print("Loop completed.")

# fruits = ["apple", "banana", "cherry", "date"]

# for index, fruit in enumerate(fruits):
#     print(index, fruit)



# # nested loop- A loop within another loop(outer, inner)
# for x in range(3):
#        for y in range(1, 10):
#         print(y, end="")



# making a Rectangle
# rows = int(input("Enter the number of rows: "))
# columns = int(input("Enter the number of columns: "))   
# symbol = input("Enter the symbol to use: ")

# for x in range(rows):
#     for y in range(columns):
#         print(symbol, end="")
#     print()
