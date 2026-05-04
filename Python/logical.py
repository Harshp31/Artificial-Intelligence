#Logical Operators

# 1- or:- atleast one true
# temp = 25
# is_raining = False

# if temp > 30 or temp < 0 or is_raining:
#     print("Outdoor Event Cancelled")
# else:
#     print("Outdoor Event Proceeding")

#in or it stops if first condition is true

# True or print("This will not be printed") # This will not be printed
# False or print("This will not be printed") # This will be printed


#and:- returns true only if both conditions are true
#not:- reverses the boolean value(not true, not false)

# temp =  2
# is_sunny = False

# if temp >= 28 and is_sunny:
#     print("Go to the beach")
# elif temp <= 0 and is_sunny:
#     print("It is cold outside")
# elif 28 > temp > 0 and is_sunny:
#     print("It's a nice day")
# elif temp >= 28 and not is_sunny:
#     print("It is cloudy")
# elif temp <= 0 and not is_sunny:
#     print("It is cold outside and cloudy")
# elif 28 > temp > 0 and not  is_sunny:
#     print("It's a nice day and cloudy")



# In and it stops if first condition is false
#False and print("This will not be printed") # This will not be printed




#Conditional expressions:- A one-liner if-else statement
# Syntax: X if condition else Y

# num = 5
# a = 4
# b = 2

# print("Positive" if num > 0 else "Negative")

# result  = "Even" if num % 2 == 0 else "Odd"
# print(result)

# max_num = a if a > b else b
# min_num = a if a < b else b
# print("Max number: ", max_num)
# print("Min number: ", min_num)  


# age = 25

# status = "Adult" if age >= 18 else "Minor"
# print(status)   


