import math

# # print(math.pi)
# # print(math.e)

# # x = 9.9
# # # result = math.sqrt(x) # This calculates the square root of x
# # #result = math.ceil(x) # This calculates the ceiling of x
# # result = math.floor(x) # This calculates the floor of x

# # print(result)


# # Exercise - Circumference of a Circle

# # radius = float(input("Enter the radius of a circle: "))

# # circumference = 2 * math.pi * radius

# # print(f"The circumference of the circle is: {round(circumference)} cm")

# # Write a program to calculate the area of a circle

# radius = float(input("Enter the radius of a circle: "))

# # area = math.pi * radius ** 2
# area = math.pi * pow(radius, 2) # This is another way to calculate the area of a circle using the pow function

# print(f"The area of the circle is: {round(area)} cm²")


# Excercise-5 hypotenous of right angle triangle

# a = float(input("Enter the length of the first side of a right angle triangle: "))
# b = float(input("Enter the length of the second side of a right angle triangle: "))

# c = math.sqrt(pow(a,2) + pow(b, 2))

# print(f"The length of the hypotenous is: {round(c)} cm")



#Scope resolution:- Follows LEGB rule

# def func1():
#     a = 10
#     print(a)

# def func2():
#     b = 20
#     print(b)


# func1()
# func2()

# def func1():
#     x = 1

#     def func2():
#        x = 2
#        print(x)
#     func2()

# func1()


# Global Scope

# def func1():
#     print(x)

# def func2():
#     print(x)

# x = 1
# func1()
# func2()
