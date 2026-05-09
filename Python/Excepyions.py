#Exception:- An event that interrupts the flow of the program.
#Exception handling:- It Prevents program from crashing

# try:
#     num = 10/0 #risky line
# except ZeroDivisionError:
#     print("Oops! Can't divide by zero")



try:
    number = int(input("Enter a number: "))
    print(1 / number)
except ZeroDivisionError:
    print("You can't divide by zero")
except ValueError:
    print("please enter number")
except Exception:
    print("something went wrong")
finally:
    print("Do some cleanup")