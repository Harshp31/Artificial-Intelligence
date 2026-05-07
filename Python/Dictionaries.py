import random
#Dictionary: A Collection of {key: value} pairs ordered and changeable. No Duplicates

# capitals = {"India": "New Delhi", 
#             "USA": "Washington DC", 
#             "France": "Paris", 
#             "Japan": "Tokyo"}

# print(dir(capitals))
# print(help(capitals))

# print(capitals.get("India")) # New Delhi


# if capitals.get("China"):
#     print("That Capital exists")
# else:
#     print("That Capital does not exist")


# capitals.update({"China": "Beijing"}) # Adds a new key-value pair to the dictionary
# print(capitals)


# capitals.pop("France") # Removes the key-value pair with the specified key(REMOVE VALUE FROM EXISTING MEMORY NOT FROM NEW ADDED)

# capitals.popitem() # Removes the last inserted key-value pair from the dictionary
# print(capitals)


# keys = capitals.keys() # Returns a view object that displays a list of all the keys in the dictionary
# # print(keys)

# for key in capitals.keys():
#     print(key)


# values = capitals.values() # Returns a view object that displays a list of all the values in the dictionary
# print(values)


# for value in capitals.values():
#     print(value)

# items = capitals.items() # Returns a view object that displays a list of all the key-value pairs in the dictionary as tuples
# print(items)

# for key, value in capitals.items():
#     print(f"{key}: {value}")



#Concession Stand Program

# menu = {
    # "Hot Dog": 3.50,
#     "Popcorn": 2.50,
#     "Soda": 1.50,
#     "Candy": 1.00,
#     "Pizza": 2.00,
#     "Lemonade": 1.50
# }

# cart = []
# total = 0


# print("------------MENU------------")
# for key, value in menu.items():
#     print(f"{key:10}: ${value:.2f}")
# print("----------------------------")


# while True:
#     food = input("Enter a food to buy (q to quit): ")
#     if food.lower() == "q":
#         break
#     if food in menu:
#         cart.append(food)
#         total += menu[food]
#     else:
#         print("That item is not on the menu. Please try again.")
#         continue

# print("------Your Cart-------")
# for item in cart:
#     print(item)
# print(f"Total: ${total:.2f}")


# while True:
#     food = input("Enter a food to buy (q to quit): ")
#     if food.lower() == "q":
#         break
#     elif menu.get(food) is not None:
#         cart.append(food)

# for food in cart:
#     total += menu.get(food)
#     print(food, end=" ")

# print()
# print(f"Total: ${total:.2f}")



#Random Number Methods

# print(random.randint(1, 100))

# number = random.randint(1, 20)
# print(number)

# low = 1
# high = 20
# number = random.randint(low, high)
# print(number)


# options = ["Rock", "Paper", "Scissors"]
# option = random.choice(options)
# print(option)


# cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
# random.shuffle(cards)
# print(cards)



# Number Guessing Game 

# lowest = 1
# highest = 100
# answer = random.randint(lowest, highest)
# guesses = 0
# is_running = True

# print("Python Number guessing Game")
# print(f"Select a number between {lowest} and {highest}")

# while is_running:
    # guess = input("Enter your guess: ")

    # if guess.isdigit():
    #     guess = int(guess)
    #     guesses += 1

    #     if guess < lowest or guess > highest:
    #         print("This Number is out of range")
    #         print(f"Select a number between {lowest} and {highest}")
    #     # if guess < lowest:
    #     #     print("This Number is too low")
    #     # elif guess > highest:
    #     #     print("This Number is too high")
    #     else:
    #         print(f"The correct number is {answer}")
    #         is_running = False

    # else:
    #     print("Invalid Guess")
    #     print(f"Select a number between {lowest} and {highest}")



# Rock Paper Scissor game

options = ["Rock", "Paper", "Scissors"]

running = True

while running:
    player = None 
    computer = random.choice(options)
   
    
    while player not in options:
        player = input("Enter your choice (Rock, Paper, Scissors): ")
        print(f"Player: {player}")
        print(f"Computer: {computer}")
        if player == computer:
            print("It's a tie!")
        elif (player == "Paper" and computer == "Rock"):
                print("You win!")
        elif(player == "Scissors" and computer == "Paper"):
            print("You win!")
        elif(player == "Rock" and computer == "Scissors"):
            print("You win!")
        elif(player == "Paper" and computer == "Scissors"):
            print("You lose!")
        elif(player == "Scissors" and computer == "Rock"):
            print("You lose!")
        elif(player == "Rock" and computer == "Paper"):
            print("You lose!")
        else:
            print("Invalid choice")

        if not input("Play again?? (y/n): ").lower() == "y":
            running = False
# # elif (player == "Rock" and computer == "Scissors") or (player == "Paper" and computer == "Rock") or (player == "Scissors" and computer == "Paper"):
#     print("You win!")

print("Thanks for playing!")
