# age = int(input("Enter your age: "))

# if age >= 18:
#     print("you are signed up!")
# elif age < 0:
#     print("Invalid age.")
# else:
#     print("you are not eligible to sign up.")



# response = input("Would ypu like food? (y/n):")

# if response == "y":
#     print("Here is your food!")
# else:
#     print("Sorry, we don't have food for you.")



# name = input("Enter your name: ")

# if name == "":
#     print("Name cannot be empty.")
# else:
#     # print("Hello, " + name + "!")
#     print(f"Hello, {name}!")



# for_sale = True

# if for_sale:
#     print("This item is for sale.")
# else:
#     print("This item is not for sale.")

# Match-case statement

# def day_of_week(day):
#     if day == "1":
#         return "Sunday"
#     elif day == "2":
#         return "Monday"
#     elif day == "3":
# #         return "Tuesday"
#     elif day == "4":
#         return "Wednesday"
#     elif day == "5":
#         return "Thursday"
#     elif day == "6":
#         return "Friday"
#     elif day == "7":
#         return "Saturday"
#     else:
#         return "Invalid day"

# print(day_of_week("1"))

# def day_of_week(day):
#     match day:
#         case "1":
#             return "Sunday"
#         case "2":
#             return "Monday"
#         case "3":
#             return "Tuesday"
#         case "4":
#             return "Wednesday"
#         case "5":
#             return "Thursday"
#         case "6":
#             return "Friday"
#         case "7":
#             return "Saturday"
#         case _:
#             return "Invalid day"

# print(day_of_week("1"))


# def is_weekend(day):
#     match day:
#         case "Saturday" | "Sunday":
#             return True
#         case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
#             return False
#         case _:
#             return False    
    
# print(is_weekend("Saturday"))