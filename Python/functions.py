#functions:- A block of reusable code 
            #Place() after the function name to invoke it

# def greet_user(username):
#     print(f"Hello! {username.title()}, Welcome to our platform.")

# greet_user("Alice")


# def happy_birthday(name, age):
#     print(f"Happy Birthday, {name}!")
#     print(f"You are now {age} years old!")

# happy_birthday("Alice", 21)


# def display_invoice(usename, amount,  due_date):
#     print(f"Hello! {usename}")
#     print(f"Your bill of {amount:.2f} is due: {due_date} ")

# display_invoice("Alice", 150.75, "2023-10-31")
# display_invoice("Bob", 200.50, "2023-11-15")
# display_invoice("Charlie", 300.00, "2023-12-01")


# return:- Statement used to end a function and send a information back to the caller
# def add(a, b):
#     z = a + b
#     return z

# def subtract(a, b):
#     z = a - b
#     return z

# def multiply(a, b):
#     z = a * b
#     return z

# def divide(a, b):
#     z = a / b
#     return z

# print(add(10, 5))
# print(subtract(10, 5))
# print(multiply(10, 5))
# print(divide(10, 5))


# def create_name(first, last):
#     first = first.capitalize()
#     last = last.capitalize()
#     return first + " " + last

# print(create_name("Harsh", "Panwar"))


# import time

# def count(start, end):

#     for x in range(start, end + 1):
#         print(x)
#         time.sleep(1)
#     print("Done!")


# count(1, 5)


# Default Arguments
#1- Default

# def net_price(list_price, discount = 0, tax = 0.05):
#     return list_price * (1 - discount) * (1 + tax)

# print(net_price(500))

# 2- keyword arguments

# def hello(greeting, title, first, last):
#     print(f"{greeting} {title} {first} {last}")

# # hello("hello", "Mr.", "Harsh", "Panwar")
# hello("hello", title="Mr.", first="Harsh", last="Panwar")


# def get_phone(country, area, first, last):
#     return f"{country}-{area}-{first}-{last}"

# phone_num = get_phone(country=+91, area=251315, first=723, last=4880)

# print(phone_num)

# *args and **kwargs

# def add(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     return total

# print(add(1, 2, 3, 4))


# def display_name(*args):
#     for arg in args:
#         print(arg, end = "")
    
# display_name("Mr.", "Harsh", "Panwar")


# **kwargs 

# def print_address(**kwargs):
#     for key, value in kwargs.keys():
#         print(f"{key}: {value}")


# print_address(street = "123",
#                city = "gautam buddha",
#                  state= "Uttar Pradesh",
#                    code= "201310",)



def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg)
    print()
    # for value in kwargs.values():
    #     print(value)
    print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('code')}")


shipping_label("123", "gautam buddha", "Uttar Pradesh", "201310", street="123", city="gautam buddha", state="Uttar Pradesh", code="201310")

